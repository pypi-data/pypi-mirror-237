# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import logging
from pathlib import Path
from typing import Callable, Union

from promptflow import PFClient
from promptflow._sdk._constants import LOGGER_NAME
from promptflow._sdk._load_functions import load_flow
from promptflow._sdk._serving._errors import UnexpectedConnectionProviderReturn, UnsupportedConnectionProvider
from promptflow._sdk._serving.utils import validate_request_data
from promptflow._sdk._utils import (
    dump_flow_result,
    get_local_connections_from_executable,
    override_connection_config_with_environment_variable,
    resolve_connections_environment_variable_reference,
    update_environment_variables_with_connections,
    print_yellow_warning,
)
from promptflow._sdk.entities._connection import _Connection
from promptflow._sdk.entities._flow import Flow
from promptflow._sdk.operations._flow_operations import FlowOperations
from promptflow._utils.multimedia_utils import convert_multimedia_data_to_base64, persist_multimedia_data
from promptflow.executor import FlowExecutor
from promptflow.storage._run_storage import DefaultRunStorage

logger = logging.getLogger(LOGGER_NAME)


class FlowInvoker:
    """
    The invoker of a flow.

    :param flow: The path of the flow, or the flow loaded by load_flow().
    :type flow: [str, ~promptflow._sdk.entities._flow.Flow]
    :param connection_provider: The connection provider, defaults to None
    :type connection_provider: [str, Callable], optional
    :param streaming: The function or bool to determine enable streaming or not, defaults to lambda: False
    :type streaming: Union[Callable[[], bool], bool], optional
    """

    def __init__(
        self,
        flow: [str, Flow],
        connection_provider: [str, Callable] = None,
        streaming: Union[Callable[[], bool], bool] = False,
        **kwargs,
    ):
        self.flow_entity = flow if isinstance(flow, Flow) else load_flow(source=flow)
        self.streaming = streaming if isinstance(streaming, Callable) else lambda: streaming
        # Pass dump_to path to dump flow result for extension.
        self._dump_to = kwargs.get("dump_to", None)

        self._init_connections(connection_provider)
        self._init_executor()
        self.flow = self.executor._flow
        self._dump_file_prefix = "chat" if self._is_chat_flow else "flow"

    def _init_connections(self, connection_provider):
        executable = self.flow_entity._init_executable()
        self._is_chat_flow, _, _ = FlowOperations._is_chat_flow(executable)
        connection_provider = "local" if connection_provider is None else connection_provider
        if isinstance(connection_provider, str):
            logger.info(f"Getting connections from pf client with provider {connection_provider}...")
            # Note: The connection here could be local or workspace, depends on the connection.provider in pf.yaml.
            self.connections = get_local_connections_from_executable(
                executable=self.flow_entity._init_executable(),
                client=PFClient(config={"connection.provider": connection_provider}),
            )
        elif isinstance(connection_provider, Callable):
            logger.info("Getting connections from custom connection provider...")
            connection_list = connection_provider()
            if not isinstance(connection_list, list):
                raise UnexpectedConnectionProviderReturn(
                    f"Connection provider {connection_provider} should return a list of connections."
                )
            if any(not isinstance(item, _Connection) for item in connection_list):
                raise UnexpectedConnectionProviderReturn(
                    f"All items returned by {connection_provider} should be connection type, got {connection_list}."
                )
            self.connections = {item.name: item.to_execution_connection_dict() for item in connection_list}
        else:
            raise UnsupportedConnectionProvider(connection_provider)

        override_connection_config_with_environment_variable(self.connections)
        resolve_connections_environment_variable_reference(self.connections)
        update_environment_variables_with_connections(self.connections)
        logger.info(f"Promptflow get connections successfully. keys: {self.connections.keys()}")

    def _init_executor(self):
        logger.info("Promptflow executor starts initializing...")
        storage = None
        if self._dump_to:
            storage = DefaultRunStorage(base_dir=self._dump_to, sub_dir=Path(".promptflow/intermediate"))
        self.executor = FlowExecutor.create(
            flow_file=self.flow_entity.path,
            working_dir=self.flow_entity.code,
            connections=self.connections,
            raise_ex=True,
            storage=storage,
        )
        self.executor.enable_streaming_for_llm_flow(self.streaming)
        logger.info("Promptflow executor initiated successfully.")

    def invoke(self, data: dict):
        """
        Process a flow request in the runtime.

        :param data: The request data dict with flow input as keys, for example: {"question": "What is ChatGPT?"}.
        :type data: dict
        :return: The flow output dict, for example: {"answer": "ChatGPT is a chatbot."}.
        :rtype: dict
        """
        logger.info(f"PromptFlow invoker received data: {data}")

        logger.info(f"Validating flow input with data {data!r}")
        validate_request_data(self.flow, data)
        logger.info(f"Execute flow with data {data!r}")
        result = self.executor.exec_line(data, allow_generator_output=self.streaming())
        # Get base64 for multi modal object
        resolved_outputs = {k: convert_multimedia_data_to_base64(v, with_type=True) for k, v in result.output.items()}
        if self._dump_to:
            result.output = persist_multimedia_data(
                result.output, base_dir=self._dump_to, sub_dir=Path(".promptflow/output")
            )
            dump_flow_result(flow_folder=self._dump_to, flow_result=result, prefix=self._dump_file_prefix)
        print_yellow_warning(f"Result: {result.output}")
        return resolved_outputs

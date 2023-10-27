from dataclasses import asdict
from dacite import from_dict


import msgpack
import zmq

from zmq_ai_client_python.schema.completion import (
    ChatCompletion)
from zmq_ai_client_python.schema.request import (
    ChatCompletionRequest,
    RequestType,
    SessionStateRequest)
from zmq_ai_client_python.schema.session_state import SessionStateResponse


class LlamaClient:
    """
    LlamaClient is a client class to communicate with a server using ZeroMQ and MessagePack.
    """

    def __init__(self, host: str):
        """
        Initializes the LlamaClient with the given host.

        :param host: The server host to connect to.
        """
        self.context = zmq.Context()  # Creating a new ZeroMQ context
        self.socket = self.context.socket(zmq.REQ)  # Creating a new request socket
        self.socket.connect(host)  # Connecting to the provided host

    def _send_request(self, request_type: RequestType, request) -> dict:
        """
        Sends a request to the server and receives a response.

        :param request_type: The type of the request.
        :param request: The request object to be sent.
        :return: The unpacked response.
        """
        packed_request = bytes([request_type.value]) + msgpack.packb(asdict(request))
        self.socket.send(packed_request)
        response = self.socket.recv()
        return msgpack.unpackb(response, raw=False)

    def send_chat_completion_request(self, request: ChatCompletionRequest) -> ChatCompletion:
        """
        Sends a ChatCompletionRequest to the server and receives a ChatCompletion.

        :param request: The request object to be sent.
        :return: The unpacked response.
        """
        res_dict = self._send_request(RequestType.CHAT_COMPLETION_REQUEST, request)
        chat_completion = from_dict(ChatCompletion, res_dict)
        return chat_completion

    def send_session_state_request(self, request: SessionStateRequest) -> SessionStateResponse:
        """
        Sends a SessionStateRequest to the server and receives a SessionStateResponse.

        :param request: The request object to be sent.
        :return: The unpacked response.
        """
        res_dict = self._send_request(RequestType.SESSION_STATE_REQUEST, request)
        session_state_response = from_dict(SessionStateResponse, res_dict)
        return session_state_response

    def send_title_generation_request(self, request: ChatCompletionRequest) -> ChatCompletion:
        """
        Sends a TitleGenerationRequest to the server and receives a ChatCompletion.
        :param request: The request object to be sent.
        :return: The unpacked response.
        """
        res_dict = self._send_request(RequestType.TITLE_GENERATION_REQUEST, request)
        chat_completion = from_dict(ChatCompletion, res_dict)
        return chat_completion

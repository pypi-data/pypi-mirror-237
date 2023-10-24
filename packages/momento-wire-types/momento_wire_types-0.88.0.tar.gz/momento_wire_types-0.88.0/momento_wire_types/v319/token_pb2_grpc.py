# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import token_pb2 as token__pb2


class TokenStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateDisposableToken = channel.unary_unary(
                '/token.Token/GenerateDisposableToken',
                request_serializer=token__pb2._GenerateDisposableTokenRequest.SerializeToString,
                response_deserializer=token__pb2._GenerateDisposableTokenResponse.FromString,
                )


class TokenServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GenerateDisposableToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TokenServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateDisposableToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateDisposableToken,
                    request_deserializer=token__pb2._GenerateDisposableTokenRequest.FromString,
                    response_serializer=token__pb2._GenerateDisposableTokenResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'token.Token', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Token(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GenerateDisposableToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/token.Token/GenerateDisposableToken',
            token__pb2._GenerateDisposableTokenRequest.SerializeToString,
            token__pb2._GenerateDisposableTokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

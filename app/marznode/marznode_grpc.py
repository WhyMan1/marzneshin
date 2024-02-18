# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: app/marznode/marznode.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import app.marznode.marznode_pb2


class MarzServiceBase(abc.ABC):

    @abc.abstractmethod
    async def SyncUsers(self, stream: 'grpclib.server.Stream[app.marznode.marznode_pb2.UserData, app.marznode.marznode_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def RepopulateUsers(self, stream: 'grpclib.server.Stream[app.marznode.marznode_pb2.UsersData, app.marznode.marznode_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def FetchInbounds(self, stream: 'grpclib.server.Stream[app.marznode.marznode_pb2.Empty, app.marznode.marznode_pb2.InboundsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FetchUsersStats(self, stream: 'grpclib.server.Stream[app.marznode.marznode_pb2.Empty, app.marznode.marznode_pb2.UsersStats]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/marznode.MarzService/SyncUsers': grpclib.const.Handler(
                self.SyncUsers,
                grpclib.const.Cardinality.STREAM_UNARY,
                app.marznode.marznode_pb2.UserData,
                app.marznode.marznode_pb2.Empty,
            ),
            '/marznode.MarzService/RepopulateUsers': grpclib.const.Handler(
                self.RepopulateUsers,
                grpclib.const.Cardinality.UNARY_UNARY,
                app.marznode.marznode_pb2.UsersData,
                app.marznode.marznode_pb2.Empty,
            ),
            '/marznode.MarzService/FetchInbounds': grpclib.const.Handler(
                self.FetchInbounds,
                grpclib.const.Cardinality.UNARY_UNARY,
                app.marznode.marznode_pb2.Empty,
                app.marznode.marznode_pb2.InboundsResponse,
            ),
            '/marznode.MarzService/FetchUsersStats': grpclib.const.Handler(
                self.FetchUsersStats,
                grpclib.const.Cardinality.UNARY_UNARY,
                app.marznode.marznode_pb2.Empty,
                app.marznode.marznode_pb2.UsersStats,
            ),
        }


class MarzServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SyncUsers = grpclib.client.StreamUnaryMethod(
            channel,
            '/marznode.MarzService/SyncUsers',
            app.marznode.marznode_pb2.UserData,
            app.marznode.marznode_pb2.Empty,
        )
        self.RepopulateUsers = grpclib.client.UnaryUnaryMethod(
            channel,
            '/marznode.MarzService/RepopulateUsers',
            app.marznode.marznode_pb2.UsersData,
            app.marznode.marznode_pb2.Empty,
        )
        self.FetchInbounds = grpclib.client.UnaryUnaryMethod(
            channel,
            '/marznode.MarzService/FetchInbounds',
            app.marznode.marznode_pb2.Empty,
            app.marznode.marznode_pb2.InboundsResponse,
        )
        self.FetchUsersStats = grpclib.client.UnaryUnaryMethod(
            channel,
            '/marznode.MarzService/FetchUsersStats',
            app.marznode.marznode_pb2.Empty,
            app.marznode.marznode_pb2.UsersStats,
        )
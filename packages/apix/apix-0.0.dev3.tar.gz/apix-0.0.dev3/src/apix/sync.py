import httpx

from .base import BaseClient
from .proto import ProtoHttp, Sync, ProtoPath, T
from .dto import Request, Response
from .serializer.base import check_response


class SyncHttp(ProtoHttp[Sync]):
    def __init__(self) -> None:
        self.__client = httpx.Client()

    def fetch(self, request: Request) -> Response:
        resp = self.__client.request(
            method=request.method,
            url=request.url,
            params=request.params,
            headers=request.headers,
            content=request.content
        )
        return Response(
            status=resp.status_code,
            content=resp.content 
        )



class SyncClient(BaseClient[Sync]):
    def __call__(self, path: ProtoPath[T], **kwargs) -> T:
        request = path.build_request(self)
        resp = check_response(self.http.fetch(request))
        return path.build_result(resp, self)

    def default_http(self) -> ProtoHttp[Sync]:
        return SyncHttp()

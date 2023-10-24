import httpx
from .base import BaseClient
from .proto import Async, ProtoHttp, ProtoPath, T
from .dto import Request, Response
from .serializer.base import check_response


class AsyncHttp(ProtoHttp[Async]):
    def __init__(self) -> None:
        self.__client = httpx.AsyncClient()

    async def fetch(self, request: Request) -> Response:
        resp = await self.__client.request(
            method=request.method,
            url=request.url,
            params=request.params,
            headers=request.headers,
            content=request.content
        )
        return Response(
            status=resp.status_code,
            content=resp.content,
        )
    


class AsyncClient(BaseClient[Async]):
    async def __call__(self, path: ProtoPath[T], **kwargs) -> T:
        request = path.build_request(self)
        resp = check_response(await self.http.fetch(request))
        return path.build_result(resp, self)

    def default_http(self) -> ProtoHttp[Async]:
        return AsyncHttp()

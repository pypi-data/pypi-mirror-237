from ..proto import ProtoClient, T, ProtoPath
from ..dto import Response, Request



class BasePath(ProtoPath[T]):
    def build_request(self, client: ProtoClient) -> Request:
        request = Request(
            method=self.__info__.method,
            url=client.build_url(self)
        )
        if self.__info__.method == "GET":
            request.params = client.config.serializer.encode_fields(self)
        else:
            request.headers["Content-Type"] = "application/json"
            request.content = client.config.serializer.encode(self)
        return request
    
    def build_result(self, response: Response, client: ProtoClient) -> T:
        return client.config.serializer.decode(response.content, self.__info__.type)


def check_response(response: Response) -> Response:
    if response.status != 200:
        raise Exception(f"Invalid response: {response}")
    return response

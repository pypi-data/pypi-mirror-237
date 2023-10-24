import pytest

from apix.serializer.msgspec_ import MsgspecSerializer
from apix.dto import Response

from .models import Data, GetData, PostData


@pytest.fixture
def serializer():
    return MsgspecSerializer()


def test_data(serializer):
    assert serializer.encode(Data("foo", "fooson")) == b'{"key":"foo","value":"fooson"}'

def test_get_data(serializer):
    assert serializer.encode(GetData("foo")) == b'{"key":"foo"}'

def test_post_data(serializer):
    assert serializer.encode(PostData("foo", "bar")) == b'{"key":"foo","value":"bar"}'

def test_decode_data(serializer):
    assert serializer.decode(b'{"key":"foo","value":"fooson"}', Data) == Data("foo", "fooson")

def test_build_request(client):
    request = GetData("foo").build_request(client)
    assert request.method == "GET"
    assert request.url == "https://api.example.com/data"
    assert request.params == {"key": "foo"}

def test_build_result(client):
    response = Response(200, b'{"key":"foo","value":"fooson"}')
    assert GetData("foo").build_result(response, client) == Data("foo", "fooson")
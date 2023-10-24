import pytest
from apix.proto import ProtoSerializer
from apix.sync import SyncClient


@pytest.fixture
def serializer() -> ProtoSerializer:
    from apix.serializer.default import default_serializer

    return default_serializer()

@pytest.fixture
def client() -> SyncClient:
    return SyncClient()
import pytest

from clients.tests.factories import ClientFactory


@pytest.fixture
def create_client():
    return ClientFactory
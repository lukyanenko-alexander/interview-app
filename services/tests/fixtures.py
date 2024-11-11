import pytest

from services.tests.factories import ServiceFactory


@pytest.fixture
def create_service():
    return ServiceFactory
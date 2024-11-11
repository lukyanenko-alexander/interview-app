import pytest
from rest_framework.test import APIClient


pytestmark = [pytest.mark.django_db]

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_order_data(create_client, create_service):
    client = create_client()
    service = create_service()

    return {
        "services": [
            {
                "service": int(service.pk),
                "quantity": 1,
            }
        ],
        "client": str(client.pk),
        "address": "ул Пушкина 50"
    }



def test_order_creation(create_order_data):
    pass


def test_order_quantity_validation(create_order_data):
    pass
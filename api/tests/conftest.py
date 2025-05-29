import pytest
from rest_framework.test import APIClient

from core import models


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def organisation():
    yield models.Organisation.objects.create(
        inn="1234567890"
    )


@pytest.fixture
def payment_data(organisation):
    data = {
        "operation_id": "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a",
        "amount": 145000,
        "payer_inn": organisation.inn,
        "document_number": "PAY-328",
        "document_date": "2024-04-27T21:00:00Z"
    }
    yield data


@pytest.fixture
def payment(organisation):
    yield models.Payment.objects.create(**{
        "id": "ccf0a86d-041b-4991-bcf7-e2352f7b8a4a",
        "amount": 145000,
        "organisation": organisation,
        "document_number": "PAY-328",
        "document_date": "2024-04-27T21:00:00Z"
    })

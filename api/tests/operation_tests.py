from rest_framework.test import APIClient
from rest_framework import status
from core import models
import pytest


@pytest.fixture
def api_client():
    return APIClient()


pytestmark = [pytest.mark.django_db]


@pytest.mark.django_db
class TestWebhookProcessor:
    endpoint = '/api/webhook/bank'

    def test_create_payment(self, payment_data, api_client):
        response = api_client.post(self.endpoint, data=payment_data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == payment_data

    def test_duplicated_payment(self, payment_data, payment, api_client):
        response = api_client.post(self.endpoint, data=payment_data)

        assert response.status_code == status.HTTP_200_OK
        assert models.Payment.objects.filter(id=payment_data.get('operation_id')).count() == 1

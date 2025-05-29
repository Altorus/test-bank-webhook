from rest_framework import status

import pytest

pytestmark = [pytest.mark.django_db]


@pytest.mark.django_db
class TestOrganisation:
    endpoint = '/api/organisations/%s/balance/'
    payment_endpoint = '/api/webhook/bank'

    def test_organisation_balance(self, organisation, api_client):
        response = api_client.get(self.endpoint % organisation.inn)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            "inn": organisation.inn,
            "balance": 0
        }
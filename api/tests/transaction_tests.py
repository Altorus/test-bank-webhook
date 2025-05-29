from rest_framework import status

import pytest

pytestmark = [pytest.mark.django_db]


@pytest.mark.django_db
class TestTransaction:
    endpoint = '/api/organisations/%s/balance/'
    payment_endpoint = '/api/webhook/bank'

    def test_log_balance(self, mocker, api_client, payment_data):
        mock_increment = mocker.patch('core.models.Organisation.increment_balance', autospec=True)
        api_client.post(self.payment_endpoint, data=payment_data)
        assert mock_increment.call_count == 1
        _, amount = mock_increment.call_args[0]
        assert amount == payment_data['amount']

    def test_increment_balance(self, mocker, organisation, api_client, payment_data):
        organisation.balance = 100
        organisation.save()

        mock_transaction = mocker.patch('core.models.Transaction.objects.create')

        api_client.post(self.payment_endpoint, data=payment_data)

        mock_transaction.assert_called()
        _, kwargs = mock_transaction.call_args
        assert kwargs['organisation'] == organisation
        assert kwargs['old_value'] == 100
        assert kwargs['new_value'] == 100 + payment_data['amount']


from rest_framework import exceptions


class PaymentDuplicationException(exceptions.APIException):
    default_detail = "Транзакция с таким идентификатором уже существует"
    status_code = 400

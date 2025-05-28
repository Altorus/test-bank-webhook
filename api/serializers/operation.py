from rest_framework import serializers
from core import models
from api import exceptions


class PaymentSerializer(serializers.ModelSerializer):
    operation_id = serializers.UUIDField(source='id')
    payer_inn = serializers.SlugRelatedField(
        slug_field='inn',
        queryset=models.Organisation.objects.all(),
        source='organisation'
    )

    class Meta:
        model = models.Payment
        fields = ("operation_id", "amount", 'payer_inn', 'document_number', 'document_date')

    def validate_operation_id(self, value):
        """
        Валидатор идентификатора операции, если операция с идентификатором существует,
        вызывается соответсвующее исключение
        """
        ModelClass = self.Meta.model

        if ModelClass.objects.filter(id=value).exists():
            raise exceptions.PaymentDuplicationException

        return value

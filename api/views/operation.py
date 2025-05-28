from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from api import serializers, exceptions
from core import models


class PaymentViewSet(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    model = models.Payment
    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except exceptions.PaymentDuplicationException:
            return Response(status=status.HTTP_200_OK)

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from api import serializers
from core import models


class OrganisationViewSet(viewsets.GenericViewSet):
    model = models.Organisation
    queryset = models.Organisation.objects.all()
    lookup_field = 'inn'

    def get_serializer_class(self):
        if self.action == "balance":
            return serializers.OrganisationBalanceSerializer
        return self.serializer_class


    @action(detail=True, methods=["get"])
    def balance(self, request, inn=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

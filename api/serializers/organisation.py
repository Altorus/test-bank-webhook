from rest_framework import serializers
from core import models


class OrganisationBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organisation
        fields = ("inn", "balance")

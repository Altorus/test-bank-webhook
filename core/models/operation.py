import uuid

from django.db import models
from .organisation import Organisation


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.IntegerField(default=0)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, blank=True, null=True)
    document_number = models.CharField(max_length=64, blank=True, null=True)
    document_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операции"
        ordering = ['document_date', 'id']


class Transaction(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, blank=True, null=True)
    old_value = models.IntegerField(default=0)
    new_value = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Изменение баланса"
        verbose_name_plural = "Изменения баланса"

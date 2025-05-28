from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from core import models


@receiver(post_save, sender=models.Payment)
@transaction.atomic
def update_organisation_balance(sender, instance, created, **kwargs):
    if not created:
        return

    organisation = instance.organisation
    organisation_balance = organisation.balance

    organisation.increment_balance(instance.amount)

    models.Transaction.objects.create(
        organisation=organisation,
        old_value=organisation_balance,
        new_value=organisation.balance,
    )

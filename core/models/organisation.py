from django.db import models


class Organisation(models.Model):
    inn = models.CharField(max_length=12, verbose_name="ИНН")
    balance = models.IntegerField(default=0, verbose_name="Баланс компании")

    def __str__(self):
        return self.inn

    def increment_balance(self, amount: int):
        """
        Метод обновляет баланс организации
        :param amount: сумма которую необходимо прибавить к текущему балансу
        """
        self.balance += amount
        self.save()

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

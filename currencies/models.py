from django.db import models
from django.core import validators


class ExchangeRate(models.Model):
    """Exchange rate at a given point in time"""

    target_currency = models.CharField(max_length=3, validators=[validators.MinLengthValidator(3)])
    base_currency = models.CharField(max_length=3, validators=[validators.MinLengthValidator(3)])
    rate = models.DecimalField(decimal_places=4, max_digits=4+10)
    at = models.DateTimeField()
    """Time point which the rate is valid for"""

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['target_currency', 'base_currency', 'at'], name='exchange_rate_unique')
        ]
        indexes = [
            models.Index(fields=['target_currency', 'base_currency'], name='exchange_rate_currencies')  # to query fast given exchange rate history
        ]

    def __str__(self):
        return "{0.base_currency}->{0.target_currency} {0.rate} at {0.at}".format(self)

from django.db import models

# Create your models here.
class ExchangeRate(models.Model):
    from_currency_code = models.CharField(max_length=6)
    to_currency_code = models.CharField(max_length=6)
    exchange_rate = models.DecimalField(max_digits=100, decimal_places=8)
    updated_at = models.DateTimeField()

    def __str__(self) -> str:
        return '{0}-{1}:{2}'.format(self.from_currency_code,self.to_currency_code,self.exchange_rate)
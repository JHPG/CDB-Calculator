from django.db import models


class CdiPrice(models.Model):
    """  ORM Model to store and query efficiently the CSV data """

    date = models.DateField(null=False)
    """ Using DecimalField instead of FloatField for more precision """
    trade_price = models.DecimalField(max_digits=19, decimal_places=16, null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'trade_price'], name='unique_cdi_price')
        ]





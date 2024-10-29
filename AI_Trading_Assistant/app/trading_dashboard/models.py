from django.db import models
from django.utils.translation import gettext_lazy as _

class AssetType(models.TextChoices):
    EQUITY='EQ', _("equity")
    SECURITY='SEC',_("security")
    FOREX='FX',_("forex")
    CASH='CASH',_("cash")

class Asset(models.Model):

    name=models.CharField(max_length=40)
    isin=models.CharField(max_length=48)
    type=models.CharField(max_length=4, choices=tuple(AssetType.choices))

class AssetDetails(models.Model):
    asset_id=models.IntegerField()
    last_observed_price=models.FloatField()
    volatility=models.FloatField()
    oneyear_roi=models.FloatField()

#class Strategy(models.Mode)
#class
# Create your models here.

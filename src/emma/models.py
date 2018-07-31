from django.db import models
from django.utils.translation import gettext as _


class Item(models.Model):
    id = models.IntegerField(primary_key=True, unique=False, blank=True)

    gtin = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_('Vendor code')
    )

    title = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_('Title')
    )

    price = models.IntegerField(blank=True)

    retail_price = models.IntegerField(null=True, blank=True)

    gross_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    created = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
        verbose_name=_('Created at')
    )

    updated = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('Updated at')
    )

    product_type = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_('Category')
    )

    class Meta:
        db_table = 'item'
        verbose_name = _('Item')
        verbose_name_plural = _('Items')
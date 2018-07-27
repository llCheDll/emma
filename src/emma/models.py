from django.db import models
from django.utils.translation import gettext as _


class Item(models.Model):
    vendor_code = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Vendor code')
    )

    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Title')
    )

    price = models.IntegerField()

    gross_weight = models.DecimalField()

    created = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Created at')
    )

    updated = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_('Updated at')
    )

    category = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Category')
    )

    class Meta:
        db_table = 'item'
        verbose_name = _('Item')
        verbose_name_plural = _('Items')
# Generated by Django 2.0.6 on 2018-07-31 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emma', '0003_auto_20180728_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='gtin',
            field=models.CharField(blank=True, max_length=100, verbose_name='Vendor code'),
        ),
    ]
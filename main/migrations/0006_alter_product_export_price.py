# Generated by Django 5.2.3 on 2025-07-09 12:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='export_price',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]

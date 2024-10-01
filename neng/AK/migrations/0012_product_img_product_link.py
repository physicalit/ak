# Generated by Django 5.1.1 on 2024-10-01 18:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AK', '0011_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]

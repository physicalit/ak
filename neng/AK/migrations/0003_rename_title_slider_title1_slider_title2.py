# Generated by Django 5.1.1 on 2024-09-30 22:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AK', '0002_footer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='title',
            new_name='title1',
        ),
        migrations.AddField(
            model_name='slider',
            name='title2',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]

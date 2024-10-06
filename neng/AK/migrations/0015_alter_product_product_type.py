# Generated by Django 5.1.1 on 2024-10-02 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AK', '0014_alter_product_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('hardware', 'Hardware Products'), ('software', 'Software Products '), ('services', 'Services'), ('promotions', 'Promotions')], default='physical', max_length=10),
        ),
    ]

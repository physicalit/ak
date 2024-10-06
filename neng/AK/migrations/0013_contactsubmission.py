# Generated by Django 5.1.1 on 2024-10-01 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AK', '0012_product_img_product_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

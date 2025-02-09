# Generated by Django 5.1.3 on 2024-11-17 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DriverInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=255)),
                ('bus_number', models.CharField(max_length=50)),
                ('driver_number', models.CharField(max_length=20)),
                ('qr_code_image', models.ImageField(upload_to='qr_codes/')),
            ],
        ),
    ]

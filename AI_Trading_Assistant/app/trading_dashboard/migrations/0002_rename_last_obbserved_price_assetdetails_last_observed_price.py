# Generated by Django 5.1.2 on 2024-10-25 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assetdetails',
            old_name='last_obbserved_price',
            new_name='last_observed_price',
        ),
    ]
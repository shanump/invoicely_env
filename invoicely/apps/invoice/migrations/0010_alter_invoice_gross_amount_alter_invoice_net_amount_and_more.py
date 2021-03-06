# Generated by Django 4.0.2 on 2022-03-22 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0009_alter_item_net_amount_alter_item_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='gross_amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='net_amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='vat_amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]

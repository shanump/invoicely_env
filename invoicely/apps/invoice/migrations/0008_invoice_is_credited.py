# Generated by Django 4.0.2 on 2022-03-20 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0007_alter_invoice_bankaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='is_credited',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-16 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paper_trader', '0004_transaction_cash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliostock',
            name='cash',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

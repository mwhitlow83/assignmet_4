# Generated by Django 5.1.1 on 2024-09-09 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=20)),
                ('symbol', models.CharField(max_length=5)),
                ('quantity', models.IntegerField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cash', models.DecimalField(decimal_places=2, default=1000, max_digits=10)),
            ],
        ),
    ]

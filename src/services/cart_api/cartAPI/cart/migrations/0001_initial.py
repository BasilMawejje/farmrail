# Generated by Django 3.0.6 on 2020-06-02 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_firstName', models.CharField(max_length=50)),
                ('customer_lastName', models.CharField(max_length=50)),
                ('customer_email', models.CharField(max_length=50, unique=True)),
                ('items', models.TextField()),
                ('item_quatity', models.PositiveIntegerField(default=0)),
                ('itemsTotal', models.DecimalField(decimal_places=3, default=0.0, max_digits=12)),
                ('adjustments', models.CharField(choices=[('DISC', 'Discount'), ('SHIP', 'Shipping'), ('TAX', 'Tax')], default='DISC', max_length=12)),
                ('adjustmentsTotal', models.DecimalField(decimal_places=3, default=0.0, max_digits=12)),
                ('total', models.DecimalField(decimal_places=3, default=0.0, max_digits=12)),
                ('checkOut', models.CharField(choices=[('PEN', 'Pending'), ('COM', 'Completed'), ('CAN', 'Cancelled')], default='PEN', max_length=12)),
                ('currenceCode', models.CharField(choices=[('UGX', 'Ugandan Shillings'), ('USD', 'United States Dollars'), ('GBP', 'British Pound')], default='UGX', max_length=5)),
            ],
        ),
    ]

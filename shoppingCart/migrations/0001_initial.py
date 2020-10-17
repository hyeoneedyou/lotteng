# Generated by Django 3.1.1 on 2020-10-16 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('onSaleProduct', '0002_auto_20200929_2318'),
        ('customer', '0002_auto_20200929_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer')),
                ('onSaleProduct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='onSaleProduct.onsaleproduct')),
            ],
        ),
    ]

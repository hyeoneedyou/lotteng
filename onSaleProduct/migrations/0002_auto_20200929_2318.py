# Generated by Django 3.1.1 on 2020-09-29 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onSaleProduct', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onsaleproduct',
            name='endDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='onsaleproduct',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='onsaleproduct',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.0.4 on 2020-04-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_auto_20200405_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_pricse',
            field=models.IntegerField(default=0),
        ),
    ]

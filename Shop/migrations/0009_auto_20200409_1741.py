# Generated by Django 3.0.4 on 2020-04-09 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_auto_20200409_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='contacter_desc',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='contacter_mail',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='contacter_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contact_us',
            name='contacter_phone',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]

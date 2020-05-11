# Generated by Django 3.0.4 on 2020-04-24 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0016_auto_20200423_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdated',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

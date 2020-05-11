# Generated by Django 3.0.4 on 2020-04-05 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_catagory', models.CharField(max_length=50)),
                ('product_desc', models.CharField(max_length=300)),
                ('product_pricse', models.IntegerField(default=0, max_length=50)),
                ('product_pub_date', models.DateField()),
                ('product_imag', models.ImageField(upload_to='shope/images')),
            ],
        ),
    ]

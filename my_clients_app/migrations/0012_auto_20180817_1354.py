# Generated by Django 2.0.6 on 2018-08-17 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_clients_app', '0011_auto_20180817_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calls',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Дата'),
        ),
    ]

# Generated by Django 2.0.7 on 2018-08-17 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_clients_app', '0012_auto_20180817_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calls',
            options={'verbose_name': 'дзвонки клиента', 'verbose_name_plural': 'Дзвонки клиентов'},
        ),
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Требуются ли клиенты'),
        ),
    ]

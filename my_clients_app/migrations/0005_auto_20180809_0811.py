# Generated by Django 2.0.6 on 2018-08-09 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_clients_app', '0004_auto_20180809_0750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeadminsettings',
            name='employees',
        ),
        migrations.AddField(
            model_name='employeeadminsettings',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='my_clients_app.Employee', verbose_name='Работник'),
            preserve_default=False,
        ),
    ]

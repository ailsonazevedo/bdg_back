# Generated by Django 4.0.6 on 2022-08-04 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_store_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='url',
        ),
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(help_text='Este numero será utilizado para efetuar o envio dos pedidos', max_length=100),
        ),
    ]

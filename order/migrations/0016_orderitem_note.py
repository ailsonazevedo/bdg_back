# Generated by Django 4.0.6 on 2022-08-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='note',
            field=models.TextField(blank=True, max_length=255, verbose_name='Observação:'),
        ),
    ]
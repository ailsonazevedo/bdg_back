# Generated by Django 4.0.6 on 2022-08-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_orderitem_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='note',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Observação:'),
        ),
    ]

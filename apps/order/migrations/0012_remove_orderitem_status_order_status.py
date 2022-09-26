# Generated by Django 4.0.6 on 2022-07-16 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_remove_orderitem_order_order_order_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Pedido realizado'), ('M', 'Preparando pedido'), ('E', 'Saiu para entrega')], default='P', max_length=1, verbose_name='Status do Pedido:'),
        ),
    ]
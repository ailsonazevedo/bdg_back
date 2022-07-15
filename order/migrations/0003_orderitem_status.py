# Generated by Django 4.0.6 on 2022-07-14 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_orderitem_options_alter_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('P', 'Pedido Realizado'), ('M', 'Preparando Pedido'), ('E', 'Saiu para entrega')], default='P', max_length=1),
        ),
    ]
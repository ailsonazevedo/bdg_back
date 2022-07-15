# Generated by Django 4.0.6 on 2022-07-15 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_orderitem_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Nome da Região:')),
                ('shipping_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço do Frete:')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='place',
        ),
        migrations.AddField(
            model_name='order',
            name='complement',
            field=models.CharField(default='', max_length=100, verbose_name='Complemento:'),
        ),
        migrations.AddField(
            model_name='order',
            name='district',
            field=models.CharField(default='', max_length=100, verbose_name='Bairro:'),
        ),
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.CharField(default='', max_length=50, verbose_name='Número:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='Endereço:'),
        ),
        migrations.AlterField(
            model_name='order',
            name='zipcode',
            field=models.CharField(default='', max_length=100, verbose_name='CEP:'),
        ),
        migrations.AddField(
            model_name='order',
            name='region',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='order.region'),
        ),
    ]
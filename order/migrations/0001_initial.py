# Generated by Django 4.0.6 on 2022-07-14 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0012_delete_ordered'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.basemodel')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=('products.basemodel',),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantidade:')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Preço:')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criação:')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='products.products')),
            ],
            options={
                'verbose_name': 'Ordered',
                'verbose_name_plural': 'Ordered',
                'ordering': ('-created_at',),
            },
        ),
    ]

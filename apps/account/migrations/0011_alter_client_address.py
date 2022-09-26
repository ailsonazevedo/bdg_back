# Generated by Django 4.0.6 on 2022-08-24 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_address_name_alter_address_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='account.address', verbose_name='Endereço'),
        ),
    ]
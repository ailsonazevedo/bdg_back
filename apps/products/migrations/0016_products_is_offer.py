# Generated by Django 4.0.6 on 2022-07-29 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_offer',
            field=models.BooleanField(default=False, null=True, verbose_name='Item em Promoção?'),
        ),
    ]
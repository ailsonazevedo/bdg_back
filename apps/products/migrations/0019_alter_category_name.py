# Generated by Django 4.0.6 on 2022-08-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_remove_category_slug_remove_products_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome: '),
        ),
    ]

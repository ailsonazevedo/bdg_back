# Generated by Django 4.0.6 on 2022-07-07 12:00

from django.db import migrations, models
import apps.products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_category_products_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.products.models.upload_image, verbose_name='Imagem:'),
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-06 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_category_options_alter_category_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'managed': True, 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-02 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_category_id_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
    ]

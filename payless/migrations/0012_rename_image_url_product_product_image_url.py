# Generated by Django 4.0.1 on 2022-02-21 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payless', '0011_product_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image_url',
            new_name='product_image_url',
        ),
    ]

# Generated by Django 4.0.1 on 2022-02-19 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payless', '0008_remove_product_image_grocery_headings_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.TextField(default='Chennai'),
        ),
    ]

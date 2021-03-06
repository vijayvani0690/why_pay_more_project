from django.db import models


# Create your models here.

class Product(models.Model):
    product_id = models.TextField()
    product_name = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
    unit = models.TextField()
    quantity = models.DecimalField(decimal_places=2, max_digits=20)
    link = models.URLField(blank=True)
    category = models.TextField(default='Groceries')
    sub_category_1 = models.TextField(default='Fruits & Vegetables')
    sub_category_2 = models.TextField(default='Fresh Vegetables')
    created_date = models.DateTimeField(auto_now=True)
    online_partner = models.TextField(default='jiomart')
    city = models.TextField(default='Chennai')
    image_url = models.URLField(default='/payless/images/no image.jpg')
    normalized_name = models.TextField(default='')
    normalized_category = models.TextField(default='')

class Grocery_Headings(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(default='Onion')
    image = models.ImageField(upload_to='payless/images/',default='null')
    category = models.TextField(default='Fresh Vegetables')

class Daily_Deals(models.Model):
    product_name = models.TextField()
    offer_price = models.DecimalField(decimal_places=2, max_digits=20)
    original_price = models.DecimalField(decimal_places=2, max_digits=20,blank=True)
    offer_percentage = models.DecimalField(decimal_places=2, max_digits=20,blank=True)
    link = models.URLField(blank=True)
    image_url = models.URLField(default='/payless/images/no image.jpg')
    online_partner = models.TextField(default='jiomart')
    unit = models.TextField(default="Kg")
    quantity = models.DecimalField(default=1, decimal_places=2, max_digits=20)
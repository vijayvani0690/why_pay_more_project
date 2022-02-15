from django.contrib import admin
from .models import Product
from .models import Grocery_Headings

# Register your models here.

admin.site.register(Product)
admin.site.register(Grocery_Headings)

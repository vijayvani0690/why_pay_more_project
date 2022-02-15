from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Grocery_Headings
import logging


# Create your views here.
def home(request):
    logging.info("----Loggin Started----")
    groceries = Grocery_Headings.objects.all()
    productList = []
    for grocery in groceries:
        products = Product.objects.filter(product_name__startswith=grocery.name).order_by('price')
        vendors1 = []
        for product in products:
            vendor_item = {'online_partner': product.online_partner, 'price': str(product.price), 'link': product.link}
            vendors1.append(vendor_item)
        if len(products) >0:
            new_product = {'product': products[0], 'vendors': vendors1, 'image': grocery.image}
            productList.append(new_product)
    return render(request, 'payless/home.html', {'products': productList})

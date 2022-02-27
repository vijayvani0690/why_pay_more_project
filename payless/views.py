from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Grocery_Headings
import logging


# Create your views here.
def home(request):
    logging.info("----Loggin Started----")
    city = "Chennai"
    selected_category = "Fresh Vegetables"
    if request.COOKIES is not None :
        if request.COOKIES.get("selected_city", None) != None :
            city = request.COOKIES['selected_city']
        if request.COOKIES.get("selected_category", None) != None:
            selected_category = request.COOKIES['selected_category']
    groceries = Grocery_Headings.objects.filter(category__contains=selected_category)
    productList = []
    for grocery in groceries:
        products = Product.objects.filter(city__contains=city).filter(product_name__contains=grocery.name).filter(sub_category_1__contains=selected_category).order_by('price')
        products.group_by = ['online_partner']
        vendors1 = []
        jio_found = False
        amazon_found = False
        bigbasket_found = False
        flipkart_found = False
        for product in products:
            if jio_found == False and product.online_partner == 'Jiomart':
                vendor_item = {'online_partner': product.online_partner, 'price': str(product.price),
                               'link': product.link}
                vendors1.append(vendor_item)
                jio_found = True
            if bigbasket_found == False and product.online_partner == 'Bigbasket':
                vendor_item = {'online_partner': product.online_partner, 'price': str(product.price),
                               'link': product.link}
                vendors1.append(vendor_item)
                bigbasket_found = True
            if amazon_found == False and product.online_partner == 'Amazon':
                vendor_item = {'online_partner': product.online_partner, 'price': str(product.price),
                               'link': product.link}
                vendors1.append(vendor_item)
                amazon_found = True
            if flipkart_found == False and product.online_partner == 'Flipkart':
                vendor_item = {'online_partner': product.online_partner, 'price': str(product.price),
                               'link': product.link}
                vendors1.append(vendor_item)
                flipkart_found = True
        if len(products) > 0:
            new_product = {'product': products[0], 'name': grocery.name, 'vendors': vendors1, 'image': grocery.image}
            productList.append(new_product)
    return render(request, 'payless/home.html', {'products': productList, 'selected_city': city, 'selected_category': selected_category})


def search(request):
    city = "Chennai"
    selected_category = "Fresh Vegetables"
    if request.COOKIES is not None:
        if request.COOKIES.get("selected_city", None) != None:
            city = request.COOKIES['selected_city']
        if request.COOKIES.get("selected_category", None) != None:
            selected_category = request.COOKIES['selected_category']
    search_key = request.GET.get('search').strip()
    groceries = Grocery_Headings.objects.filter(name__contains=search_key.capitalize())
    productList = []
    products = Product.objects.filter(city__contains=city).filter(product_name__contains=search_key.capitalize()).filter(sub_category_1=selected_category).order_by('price')
    jio_found = False
    amazon_found = False
    bigbasket_found = False
    for product in products:
        vendor_item = {'online_partner': product.online_partner, 'price': str(product.price), 'link': product.link}
        vendors1 = [vendor_item]
        if len(groceries) > 0:
            new_product = {'product': product, 'name': product.product_name, 'vendors': vendors1, 'image': product.image_url}
            productList.append(new_product)
        else:
            image1 = {"url": "/media/payless/images/no image.jpg"}
            new_product = {'product': product, 'name': product.product_name, 'vendors': vendors1, 'image': image1}
            productList.append(new_product)
    return render(request, 'payless/home.html', {'products': productList, 'selected_city': city, 'selected_category': selected_category })

def setcity(request):

    selected_category = request.GET.get('select_category').strip()
    city = request.GET.get('select_city').strip()
    productList = []
    groceries = Grocery_Headings.objects.filter(category__contains=selected_category)
    for grocery in groceries:
        products = Product.objects.filter(city__contains=city).filter(product_name__contains=grocery.name).filter(sub_category_1__contains=selected_category).order_by('price')
        products.group_by = ['online_partner']
        vendors1 = []
        jio_found = False
        amazon_found = False
        bigbasket_found = False
        flipkart_found = False
        for product in products:
            if jio_found == False and product.online_partner == 'Jiomart':
                vendor_item = {'online_partner': product.online_partner, 'price': str(product.price),
                               'link': product.link}
                vendors1.append(vendor_item)
                jio_found = True
            if bigbasket_found == False and product.online_partner == 'Bigbasket':
                vendor_item = {'online_partner': product.online_partner, 'price': str(product.price),
                               'link': product.link}
                vendors1.append(vendor_item)
                bigbasket_found = True
            if amazon_found == False and product.online_partner == 'Amazon':
                vendor_item = {'online_partner': product.online_partner, 'price': str(product.price),
                               'link': product.link}
                vendors1.append(vendor_item)
                amazon_found = True
            if flipkart_found == False and product.online_partner == 'Flipkart':
                vendor_item = {'online_partner': product.online_partner, 'price': str(product.price),
                               'link': product.link}
                vendors1.append(vendor_item)
                flipkart_found = True
        if len(products) > 0:
            new_product = {'product': products[0], 'name': grocery.name, 'vendors': vendors1, 'image': grocery.image}
            productList.append(new_product)
        response = render(request, 'payless/home.html', {'products': productList, 'selected_city': city, 'selected_category': selected_category})
        if request.GET.get('select_city').strip() != "":
            response.set_cookie('selected_city', request.GET.get('select_city').strip())
        if request.GET.get('select_category').strip() is not None and request.GET.get('select_category').strip() != "":
            response.set_cookie('selected_category', request.GET.get('select_category').strip())

    return response
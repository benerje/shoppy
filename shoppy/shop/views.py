from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def index(request):
    products = Product.objects.all()
    # print(products)
    # params = {'product': products, 'range': range(
    #     1, nSlides), 'no_of_slides': nSlides}

    # allProds = [[products, range(1, nSlides), nSlides], [
    #     products, range(1, nSlides), nSlides]]

    allProds = []
    # retrive category and id values in all items(array)
    catProds = Product.objects.values('category', 'id')
    cats = {item['category']
            for item in catProds}  # give the values of categories

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 * ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse('contact')


def tracker(request):
    return HttpResponse('tracker')


def search(request):
    return HttpResponse('search')


def productview(request):
    return HttpResponse('productview')


def checkout(request):
    return HttpResponse('checkout')

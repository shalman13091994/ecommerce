from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category

#we want to reflect this category in the nav bar throughout the page we just add this in the settings( under template)
# def category(request):
#     return{
#         'categories':Category.objects.all() 
#     }

def product_all(request):
    allproducts = Product.objects.all()
    return render(request, 'store/home.html', {"product": allproducts})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock =True)
    return render(request , 'store/products/single.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug =category_slug)
    product = Product.objects.filter(category = category)
    return render(request,"store/products/category.html", {'category':category,'product': product})
    




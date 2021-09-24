from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Category, Product

#
# def home(request):
#     return render(request,'home.html')


def product_all(request):
    """prefetch_related() - returns a queryset that will automatically retrieve in a single batch,
    related objects for  each of the specified lookups.
    Istead of running 2 similar queries for finding the product imange of product id=1 and 2
    we can make it in one query these can be find in 0djangodebugtoolbar"""

    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    # products = Product.objects.all()
    # products = Product.products.all()
    return render(request, "store/index.html", {"products": products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    ## we need all the producs in that respective category
    # ##  products is the product manager variable
    # products = Product.objects.filter(category=category)
    ##to get the books which are under django i.e.,., descendants
    products = Product.objects.filter(
        category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True)
    )
    return render(request, "store/category.html", {"category": category, "products": products})


def product_detail(request, pro_slug):  # slug here is the reference from the url
    # we have pro_slug that should match with this slug of te url
    product = get_object_or_404(Product, slug=pro_slug, is_active=True)
    return render(request, "store/single.html", {"product": product})

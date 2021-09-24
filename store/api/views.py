from rest_framework import generics, mixins
from store.models import Category, Product

from .serializers import (
    CategoryListSerializer,
    CategoryRUDserialiser,
    ProductDetailSerialiser,
    ProductListAPISerialiser,
)


# category list
class CategoryListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    # queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    def get_queryset(self):
        return Category.objects.all()

    # in listapi we can create a post for that we use mixins
    # to post in the category list
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    # to patch
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    
    # # to put
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)


class CategoryCreateView(generics.CreateAPIView):
    # queryset = Category.objects.all
    serializer_class = CategoryRUDserialiser

    def get_queryset(self):
        return Category.objects.all()


# RetrieveUpdateDestroyAPIView
class CategoryRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "slug"
    serializer_class = CategoryRUDserialiser

    def get_queryset(self):
        return Category.objects.all()


# product list
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListAPISerialiser


# # product detail
# class ProductDetailView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductDetailSerialiser
#     lookup_field = "slug"
#     # lookup_url_kwarg = "slug"

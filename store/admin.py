from django.contrib import admin
from django import forms
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
    ProductType,
)

admin.site.register(Category, MPTTModelAdmin)

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines=[
        ProductSpecificationInline,
    ]

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductSpecificationValueInline(admin.TabularInline):
    model =  ProductSpecificationValue

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationValueInline,
        ProductImageInline,
    ]

















# ****************************************

# from django.contrib import admin

# from .models import Category,Product

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = [ 'name', 'slug'] #model fields
#     #whatever the name we enter for the name it will be prepopulated in the slug field
#     prepopulated_fields = {'slug': ('name',)}

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = [ 'title', 'author', 'slug','price', 'in_stock', 'created', 'updated']
#     #To create a list filter for these fields
#     list_filter = ['in_stock', 'is_active']
#     list_editable = ['price', 'in_stock']
#     #whatever the title we enter for the name it will be prepopulated in the slug field
#     prepopulated_fields = {'slug': ('title',)}

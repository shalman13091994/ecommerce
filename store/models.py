from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length= 150, db_index = True)
    slug = models.SlugField(max_length=200, unique =True)

    class Meta:
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    description = models.TextField(blank=True)
    author = models.CharField(max_length = 140)
    image = models.ImageField(upload_to ='images/')
    slug = models.SlugField(max_length=180)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
 
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created']

    def __str__(self):
        return self.title



   


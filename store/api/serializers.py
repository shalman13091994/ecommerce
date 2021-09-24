# it helps to turn data into json and validation
# it works like forms
""" 
serializers in REST framework work very similarly to Django's Form and ModelForm classes. 
"""
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from store.models import Category, Product


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductListAPISerialiser(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductDetailSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategoryRUDserialiser(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
      
        # we can't change it
        # read_only_fields = ["slug", "regular_price"]
   
    # model we have designed it not to take the existing categoryname and slug
        def validate_title(self, value):
            qs = Category.objects.filter(name=value)  # including instance
            if self.instance:
                qs = qs.exclude(Category(name=self.instance.name) | Category(slug=self.instance.slug))
            if qs.exists():
                raise serializers.ValidationError("Category has been used already")
            return value

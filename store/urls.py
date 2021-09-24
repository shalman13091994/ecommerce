from django.urls import path
from.views import product_all,product_detail,category_list

app_name='store'

urlpatterns=[
    # path('',home,name='home')
    path('', product_all, name='store_home'),
    # here slug : pro_slug is the type of data: name of the variable built data will be in
    path('<slug:pro_slug>/',product_detail,name='product_detail'),
    path('shop/<slug:category_slug>/', category_list, name='category_list'),

]
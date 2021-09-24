
from django.urls import path
from .views import BasketView, order_placed, stripe_webhook

app_name = 'payment'

urlpatterns = [
    path('billing/', BasketView, name='basket'),
    path('orderplaced/', order_placed, name='order_placed'),
    path('webhook/', stripe_webhook,name='webhook'),
]

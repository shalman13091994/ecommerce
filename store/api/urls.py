from django.urls import path

from .views import (
    CategoryCreateView,
    CategoryListAPIView,
    CategoryRUDView,
    ProductListAPIView,
)

# ProductDetailView,

app_name = "store-api"

urlpatterns = [
    path("", CategoryListAPIView.as_view(), name="category_listapi"),
    path("product/", ProductListAPIView.as_view(), name="product_listapi"),
    # path("product/<slug:slug>/", ProductDetailView.as_view(), name="product_detailapi"),
    # path("product/<slug:slug>/detail/", ProductDetailView.as_view(), name="product_detailapi"),
    path("category/", CategoryCreateView.as_view(), name="category_create"),
    path("category/<slug:slug>/", CategoryRUDView.as_view(), name="category_rud"),
]

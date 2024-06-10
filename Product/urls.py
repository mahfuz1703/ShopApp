from django.urls import path
from Product import views

urlpatterns = [
    path('products', views.all_product, name="all_product"),
    path('products_details/<int:product_id>/', views.product_details, name="product_details"),
]
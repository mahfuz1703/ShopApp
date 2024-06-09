from django.urls import path
from Product import views

urlpatterns = [
    path('product', views.product, name="product"),
]
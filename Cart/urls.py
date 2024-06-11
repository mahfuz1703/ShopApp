from django.urls import path, include
from Cart import views
urlpatterns = [
    path('mycart', views.mycart, name="mycart"),
    path('add/<int:product_id>', views.add_to_cart, name="add_to_cart"),
    path('remove/<int:cart_item_id>', views.delete_to_cart, name="delete_to_cart"),
    path('update/<int:cart_item_id>', views.update_to_cart, name="update_to_cart"),
    path('increase/<int:cart_item_id>', views.increase_quantity, name="increase_quantity"),
    path('decrease/<int:cart_item_id>', views.decrease_quantity, name="decrease_quantity"),
]
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def mycart(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    try:
        user_cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        user_cart = Cart.objects.create(user=request.user)
        user_cart.save()
    items = user_cart.items.all()
    return render(request, "cart/cart.html", {'cart':user_cart, 'items':items})

def add_to_cart(request, product_id):
    user_cart = Cart.objects.get(user=request.user)
    product = Product.objects.get(id = product_id)
    user_cart.add_item(product, 1)
    return redirect('mycart')

def delete_to_cart(request, cart_item_id):
    user_cart = Cart.objects.get(user=request.user)
    user_cart.delete_item(cart_item_id)
    return redirect('mycart')

def update_to_cart(request, cart_item_id):
    user_cart = Cart.objects.get(user=request.user)
    quantity = request.POST['quantity']
    user_cart.update_item(cart_item_id, quantity)
    return redirect('mycart')

def increase_quantity(request, cart_item_id):
    user_cart = Cart.objects.get(user=request.user)
    user_cart.increase_quantity(cart_item_id)
    return redirect('mycart')

def decrease_quantity(request, cart_item_id):
    user_cart = Cart.objects.get(user=request.user)
    user_cart.decrease_quantity(cart_item_id)
    return redirect('mycart')
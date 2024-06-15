from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from Cart.models import Order
from .forms import UserProfileForm
from. models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, "home/home.html", {'user':  request.user})
    return redirect('signup')


def signup(request):
    if  request.method == "POST":
        is_login = request.POST['is_login']
        
        if is_login == '1':
            username = request.POST['login_username']
            password = request.POST['login_password']

            # print(username)
            # print(password)

            user = authenticate(username=username, password=password)
            # print(user)
            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                    return redirect(reverse('admin:index'))
                else:
                    return redirect('home')
            else:
                return HttpResponse("User not found or incorrect credentials!!")
        else:
            username = request.POST['signup_username']
            email = request.POST['signup_email']
            password = request.POST['signup_password']
            password2 = request.POST['signup_password2']
            
            if not username or not email or not password or not password2:
                return  HttpResponse("Please fill in all fields")
            if password != password2:
                return HttpResponse("Password does not match")
            elif User.objects.filter(username=username).exists():
                return HttpResponse("Username already exists")
            elif User.objects.filter(email=email).exists():
                return HttpResponse("Email already exists")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return HttpResponse(f"Welcome, {username}!!!")

    return render(request, "authentication/signup.html")

def signout(request):
    logout(request)
    return redirect('signup')

def profile(request):
    if request.user.is_authenticated:
        profile = request.user.userprofile
        return render(request, "authentication/user_profile.html", {'profile':  profile})
    return redirect('signup')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

def edit_profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        # If UserProfile doesn't exist, create a new one
        user_profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'authentication/edit_profile.html', {'form': form})


def myorders(request):
    if request.user.is_authenticated:
        try:
            orders = Order.objects.filter(user=request.user)
            has_orders = orders.exists() 
            # items = Order.items.all()
        except Order.DoesNotExist:
            return HttpResponse("Order not found")
        
        return render(request, "authentication/myorders.html", {'orders':orders, 'has_orders': has_orders})
    else:
        return redirect(signup)
    




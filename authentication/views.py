from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return HttpResponse("Welcome to ShopApp")

def signup(request):
    if  request.method == "POST":
        username = request.POST['login_username']
        password = request.POST['login_password']

        # print(username)
        # print(password)

        user = authenticate(username=username, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            return HttpResponse(f"Welcome, {username}!!!")
        else:
            if username and password:
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



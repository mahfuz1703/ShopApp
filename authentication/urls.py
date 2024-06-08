from django.urls import path
from authentication import views

urlpatterns = [
    path('signup',  views.signup, name='signup'),
    path('', views.home, name="home"),
]
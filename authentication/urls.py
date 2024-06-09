from django.urls import path
from authentication import views

urlpatterns = [
    path('signup',  views.signup, name='signup'),
    path('signout',  views.signout, name='signout'),
    path('', views.home, name="home"),
]
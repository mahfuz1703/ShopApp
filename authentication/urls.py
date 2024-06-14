from django.urls import path
from authentication import views

urlpatterns = [
    path('signup',  views.signup, name='signup'),
    path('signout',  views.signout, name='signout'),
    path('profile',  views.profile, name='profile'),
    path('myorders',  views.myorders, name='myorders'),
    path('edit_profile',  views.edit_profile, name='edit_profile'),
    path('', views.home, name="home"),
]
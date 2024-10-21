from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("Home", views.Home, name='Home'),
    path("forgot_password", views.forgot_password, name='forgot-password'),
    path("Sign_up", views.Sign_up, name='Sign_up'),
    path("", views.login, name='login'),
    path('Home',views.Home, name='Home'),
    path('logout',views.logout,name='logout.html'),
    path("profile",views.profile, name="profile.html"),
    path('setting',views.setting,name='setting.html'),
    path("Home", views.Home, name='Home'),  # Keep only one 'Home' path

    
]
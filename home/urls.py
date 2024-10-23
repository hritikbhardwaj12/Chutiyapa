from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("Sign_up", views.sign_up, name='Sign_up'),
    path("", views.login, name='login'),
    path('home',views.Home, name='home'),
    path('logout',views.logout,name='logout.html'),
    path("profile",views.profile, name="profile.html"),
    path('setting',views.setting,name='setting.html'),
    path("forgot_password", views.forgot_password, name='forgot-password'),
    path("Home", views.Home, name='Home'),  # Keep only one 'Home' path
    path("login", views.login, name='login'),

    
]
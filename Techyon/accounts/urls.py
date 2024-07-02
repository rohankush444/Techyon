from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('' ,  home  , name="home"),
    path('register' , register , name="register"),
    path('accounts/login/' , user_login , name="user_login"),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('about',about,name="about")
]
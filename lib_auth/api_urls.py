from django.contrib import admin
from django.urls import path
from lib_auth.views import *
urlpatterns = [
    path('signup/', UserCreateApi.as_view()),
    path('login/', UserLoginApi.as_view()),
]

from django.urls import path
from core.views import *
urlpatterns = [
    path('category/', CategoryApi.as_view()),

]
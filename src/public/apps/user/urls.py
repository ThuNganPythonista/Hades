from django.urls import path, include
from src.public.apps.user.views import *


urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('register/', Register.as_view(), name="register"),
]


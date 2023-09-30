from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', HomeView.as_view(),name="index-file"),
    path('footwear/', Footwear.as_view(), name="product-file"),
    path('login/', Login.as_view(), name="login"),
    path('register/', Register.as_view(), name="register-file"),

]

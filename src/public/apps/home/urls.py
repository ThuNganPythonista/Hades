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
    path('Aboutus/', AboutUs.as_view(), name="messenger-file"),
    path('news/', News.as_view(), name="news-file"),
    path('sell/', Sell.as_view(), name="sell-file"),
    path('quyengop/',Quyen.as_view(), name="quyengop-file"),
    path('map/', Map.as_view(), name="map-file"),

]

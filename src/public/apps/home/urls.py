from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(),name="index-file"),
    path('footwear/', Footwear.as_view(), name="product-file"),
    path('add-product/', AddProductView.as_view(), name="product-new"),
]

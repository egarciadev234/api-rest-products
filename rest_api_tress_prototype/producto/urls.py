from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('productos', ListProduct.as_view(), name='list-productos'),
    path('productos/<int:pk>', DetailProduct.as_view(), name='detail-producto'),
]

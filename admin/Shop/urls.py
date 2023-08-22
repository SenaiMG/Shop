from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('price/', views.price, name='produto'),
    path('cart/', views.cart, name='carrinho'),
]

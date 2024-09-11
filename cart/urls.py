from django.urls import path
from django.shortcuts import render
from . import views

app_name = 'cart'

urlpatterns = [
    path('', lambda request: render(request, 'cart/cart_detail.html'), name='cart_detail'),
    path('add/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('clear/', views.clear_cart, name='clear_cart'),
    path('update-quantity/', views.update_quantity, name='update_quantity'),
    path('remove/', views.remove_product, name='remove_product'),
]

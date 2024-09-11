from django.urls import path
from . import views
from django.shortcuts import redirect

app_name = 'shop'

urlpatterns = [
    path('', lambda request: redirect('shop:product_list'), name='index'),
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:category_slug>/', views.product_list, name='product_by_category_list'),
    path('product/', lambda request: redirect('shop:product_list')),
    path('product/<slug>', views.product_detail, name='product_detail'),

]

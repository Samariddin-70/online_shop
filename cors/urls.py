from django.urls import path
from .views import *

urlpatterns =[
    path('',index, name='home'),
    path('account/',account, name='account'),
    path('cart/',cart, name='cart'),
    path('categories/',categories, name='categories'),
    path('checkout/',checkout, name='checkout'),
    path('product_d/',product_d, name='product_d'),
    path('search/',search, name='search'),
    path('product/',product, name='product'),
]
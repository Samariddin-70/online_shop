from django.urls import path
from .views import *

urlpatterns = [
    path('sign_up/', sign_up, name='register'),
    path('sign_in/', sign_in, name='login'),
    path('sign_out',sign_out, name='sign_out')
]
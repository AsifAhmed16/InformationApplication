from django.urls import path, include
from .views import *

app_name = 'info'

urlpatterns = [
    path('', user_form, name='user_form'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('app_list/', app_list, name='app_list'),
]

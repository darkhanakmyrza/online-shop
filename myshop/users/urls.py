from django.urls import path
from . import views

app_name ='users'

urlpatterns = [
   
    path('register/', name='register'),
    path('login/', name='login'),
]
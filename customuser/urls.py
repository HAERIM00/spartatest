from django.contrib import admin
from django.urls import path
from customuser import views

urlpatterns = [
    path('user/', views.user),
]

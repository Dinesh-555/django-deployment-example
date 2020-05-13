from django.contrib import admin
from django.urls import path
from apptwo import views
urlpatterns = [
    path('',views.users,name='users'),
]
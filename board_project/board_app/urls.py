from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import path 
from . import views

urlpatterns = [
    path('register/', views.register),
    path('board_list/',views.board_list),
    path('board_detail/<int:pk>/',views.board_detail),
    path('board_update/<int:pk>/',views.board_update),
    path('board_delete/<int:pk>/',views.board_delete),
    path('',views.home),
]
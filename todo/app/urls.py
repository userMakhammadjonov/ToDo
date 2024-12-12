from django.urls import path
from django.shortcuts import redirect

from .views import show_lists,list_details,main

urlpatterns = [
    path('', lambda request: redirect('main/')),
    path('lists/',show_lists),
    path('main/',main),
    path('list-details/<int:list_id>/',list_details),
]


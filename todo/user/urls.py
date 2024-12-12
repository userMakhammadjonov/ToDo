from django.contrib.auth.views import LoginView,LogoutView

from django.urls import path

from .views import register

urlpatterns = [
    path('auth/login/',LoginView.as_view()),
    path('auth/logout/',LogoutView.as_view()),
    path('auth/register/',register),
]



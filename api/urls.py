from django.urls import path, include
from rest_framework import routers
from api import views


urlpatterns= [
    path('usuarios/<str:correo>/<str:contrasenia>/', views.UsuariosView.as_view(),name='user'),
]

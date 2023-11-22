from django.urls import path, include
from rest_framework import routers
from api import views


urlpatterns= [
    path('usuarios/<str:correo>/<str:contrasenia>/', views.UsuariosView.as_view(),name='user'),
    path('usuariopost/',views.UsuarioCreateView.as_view(), name='crearuser'),
    path('enfermedades/', views.EnfermesadViewList.as_view(), name='enfermedades'),
    path('menus/<int:id_perfil>',views.MenuViewList.as_view(), name='menus'),
]

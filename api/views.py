from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.decorators import api_view
from rest_framework.views import View
from django.http.response import JsonResponse
# Create your views here.

class UsuariosView(View):

    def get(self,request, correo, contrasenia):
        usuarios = list(Usuario.objects.filter(correo=correo, contrasenia=contrasenia).values())
        if len(usuarios)>0:
            credenciales = usuarios[0]
            datos ={ 'message':'success', 'usuarios':credenciales}
        else:
            datos ={'messages':'Usuarios no encontrados'}
        return JsonResponse(datos)
from typing import Any
from django import http
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializer import *
from django.utils.decorators import method_decorator
from rest_framework.views import View
from django.http.response import JsonResponse
# Create your views here.

class UsuariosView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, correo, contrasenia):
        usuarios = list(Usuario.objects.filter(correo=correo, contrasenia=contrasenia).values())
        if len(usuarios)>0:
            credenciales = usuarios[0]
            datos ={ 'message':'success', 'usuarios':credenciales}
        else:
            datos ={'messages':'Usuarios no encontrados'}
        return JsonResponse(datos)
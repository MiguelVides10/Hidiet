from typing import Any
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializer import *
from django.utils.decorators import method_decorator
from rest_framework.views import View
from django.http.response import JsonResponse
import json
from django.db import connection
from rest_framework import generics
# Create your views here.

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


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
            datos ={'error':'Usuario no encontrados'}
        return JsonResponse(datos)
    

class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            datos ={'message':'usuario creado'}
            return JsonResponse(datos)
        else:
            datos ={'message':'No se guardo la info'}
            return JsonResponse(datos)
        
class EnfermesadViewList(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        enfermedades = list(Enfermedad.objects.values())
        if len(enfermedades)>0:
            datos ={ 'message':'success', 'enfermedades':enfermedades}
        else:
            datos ={'error':'No hay datos'}
        return JsonResponse(datos)
    
class MenuViewList(View):
    def get(self, request, id_perfil):
        lookup_field = 'id_perfil'
        with connection.cursor() as cursor:
            cursor.execute("SELECT desayuno, almuerzo, cena FROM hidiet.menu m inner join hidiet.perfil p on p.id_menu = m.id_menu where p.id_perfil = %s;", [id_perfil])
            rows = dictfetchall(cursor)
            datos ={ 'message':'success', 'menu':rows}
            return JsonResponse(datos)

class PerfilViewList(View):
    def get(self, request, id_usuario):
        lookup_field = 'id_usuario'
        with connection.cursor() as cursor:
            cursor.execute("SELECT u.correo, p.sexo, p.peso, p.estatura FROM hidiet.perfil p inner join hidiet.usuario u on p.id_user = u.id_usuario where p.id_user=%s;", [id_usuario])
            rows = dictfetchall(cursor)
            datos ={ 'message':'success', 'perfil':rows}
            return JsonResponse(datos)


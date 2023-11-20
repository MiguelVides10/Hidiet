from rest_framework import serializers
from .models import *


class EnfermedadSerializer (serializers.ModelSerializer):
    class Meta:
        model = Enfermedad
        fields = '__all__'

class MenuSerializer (serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class PerfilSerializer (serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class ProgresoSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Progreso
        fields = '__all__'

class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
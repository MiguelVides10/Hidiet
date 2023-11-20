# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Enfermedad(models.Model):
    id_enfer = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    consejo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enfermedad'


class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    desayuno = models.CharField(max_length=800, blank=True, null=True)
    almuerzo = models.CharField(max_length=800, blank=True, null=True)
    cena = models.CharField(max_length=800, blank=True, null=True)
    dia = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'


class Perfil(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    peso = models.FloatField()
    estatura = models.FloatField(blank=True, null=True)
    sexo = models.CharField(max_length=45, blank=True, null=True)
    objetivos = models.CharField(max_length=200, blank=True, null=True)
    id_enfer = models.ForeignKey(Enfermedad, models.DO_NOTHING, db_column='id_enfer', blank=True, null=True)
    id_user = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    id_menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='id_menu', blank=True, null=True)
    id_progreso = models.ForeignKey('Progreso', models.DO_NOTHING, db_column='id_progreso', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfil'


class Progreso(models.Model):
    id_progreso = models.AutoField(primary_key=True)
    calorias = models.CharField(max_length=45, blank=True, null=True)
    peso_act = models.CharField(max_length=45, blank=True, null=True)
    ejercicio = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'progreso'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    correo = models.CharField(max_length=45)
    contrasenia = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'usuario'

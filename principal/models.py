#encoding:utf-8

from django.db import models

# Create your models here.

class Banco(models.Model):
    entidadId = models.DecimalField(max_digits=4, unique=True)
    nombre = models.CharField()

    def __unicode__(self):
        return self.entidadId

class Sucursal(models.Model):
    sucursalId = models.DecimalField(max_digits=4, unique=True)
    entidad = models.ForeignKey(Banco)
    direccion = models.CharField()
    telefono = models.CharField()

    def __unicode__(self):
        return self.sucursalId

class Usuario(models.Model):
    nombreUsuario = models.CharField(unique=True)
    password = models.CharField()
    email = models.EmailField()
    nombre = models.CharField()
    apellidos = models.CharField()

    def __unicode__(self):
        return self.nombreUsuario

class Cuenta(models.Model):
    numeroCuenta = models.DecimalField(max_digits=20, unique=True)
    usuarios = models.ForeignKey(Usuario)
    saldo = models.CharField()

    def __unicode__(self):
        return self.numeroCuenta

class TipoMovimiento(models.Model):
    tipoMovId = models.CharField(unique=True)
    descripcion = models.TextField(help_text='Transferencia, recibo, nómina, extracción en cajero')

    def __unicode__(self):
        return self.tipoMovId

class Movimiento(models.Model):
    fecha = models.DateTimeField()
    numeroCuenta = models.ForeignKey(Cuenta)
    descripcion = models.TextField()
    tipoMov = models.ForeignKey(TipoMovimiento)
    euros = models.CharField()

    def __unicode__(self):
        return self.tipoMov

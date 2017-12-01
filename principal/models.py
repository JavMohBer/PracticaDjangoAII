#encoding:utf-8

from django.db import models

# Create your models here.

class Banco(models.Model):
    entidadId = models.DecimalField(max_digits=4, unique=True, decimal_places=0)
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.entidadId

class Sucursal(models.Model):
    sucursalId = models.DecimalField(max_digits=4, unique=True, decimal_places=0)
    entidad = models.ForeignKey(Banco)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=9)

    def __unicode__(self):
        return self.sucursalId

class Usuario(models.Model):
    nombreUsuario = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombreUsuario

class Cuenta(models.Model):
    numeroCuenta = models.DecimalField(max_digits=20, unique=True, decimal_places=0)
    usuarios = models.ForeignKey(Usuario)
    saldo = models.DecimalField(max_digits=100000000000, decimal_places=100000000000)

    def __unicode__(self):
        return self.numeroCuenta

class TipoMovimiento(models.Model):
    tipoMovId = models.CharField(unique=True, max_length=50)
    descripcion = models.TextField(help_text='Transferencia, recibo, nómina, extracción en cajero')

    def __unicode__(self):
        return self.tipoMovId

class Movimiento(models.Model):
    fecha = models.DateTimeField()
    numeroCuenta = models.ForeignKey(Cuenta)
    descripcion = models.TextField()
    tipoMov = models.ForeignKey(TipoMovimiento)
    euros = models.DecimalField(max_digits=100000000000, decimal_places=100000000000)

    def __unicode__(self):
        return self.tipoMov

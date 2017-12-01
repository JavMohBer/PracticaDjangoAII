from django.forms import ModelForm
from django import forms
from principal.models import *

class BancoForm(ModelForm):
    class Meta:
        entidadId = forms.DecimalField(max_digits=4)
        nombre = forms.CharField()

class SucursalForm(ModelForm):
    class Meta:
        sucursalId = forms.DecimalField(max_digits=4)
        entidad = forms.ForeignKey(Banco)
        direccion = forms.CharField()
        telefono = forms.CharField()

class UsuarioForm(ModelForm):
    class Meta:
        nombreUsuario = forms.CharField()
        password = forms.PasswordInput()
        email = forms.EmailField()
        nombre = forms.CharField()
        apellidos = forms.CharField()

class CuentaForm(ModelForm):
    class Meta:
        numeroCuenta = forms.DecimalField(max_digits=20)
        usuarios = forms.ForeignKey(Usuario)
        saldo = forms.CharField()

class TipoMovimientoForm(ModelForm):
    class Meta:
        tipoMovId = forms.CharField()
        descripcion = forms.Textarea()

class MovimientoForm(ModelForm):
    class Meta:
        fecha = forms.DateTimeField()
        numeroCuenta = forms.ForeignKey(Cuenta)
        descripcion = forms.TextField()
        tipoMov = forms.ForeignKey(TipoMovimiento)
        euros = forms.CharField()
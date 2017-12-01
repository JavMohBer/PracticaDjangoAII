from django.forms import ModelForm
from principal.models import *

class BancoForm(ModelForm):
    class Meta:
        model = Banco
        fields = ['entidadId', 'nombre']

class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = ['sucursalId', 'entidad', 'direccion', 'telefono']

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombreUsuario', 'password', 'email', 'nombre', 'apellidos']

class CuentaForm(ModelForm):
    class Meta:
        model = Cuenta
        fields = ['numeroCuenta', 'usuarios', 'saldo']

class TipoMovimientoForm(ModelForm):
    class Meta:
        model = TipoMovimiento
        fields = ['tipoMovId', 'descripcion']

class MovimientoForm(ModelForm):
    class Meta:
        model = Movimiento
        fields = ['fecha', 'numeroCuenta', 'descripcion', 'tipoMov', 'euros']
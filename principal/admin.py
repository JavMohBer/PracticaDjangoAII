from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Banco)
admin.site.register(Sucursal)
admin.site.register(Usuario)
admin.site.register(Cuenta)
admin.site.register(TipoMovimiento)
admin.site.register(Movimiento)



from django.contrib import admin

# Register your models here.

from .models import Receta, Usuario, Blog

admin.site.register(Receta)
admin.site.register(Usuario)
admin.site.register(Blog)


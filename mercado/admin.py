from django.contrib import admin

from mercado.models import Categoria, Marca, Carne, Laticínio


admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Carne)
admin.site.register(Laticínio)
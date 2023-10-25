from django.contrib import admin

from mercado.models import Categoria, Marca, Carne, Laticínio, Fruta, Legume, Verdura, Bebida

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Carne)
admin.site.register(Laticínio)
admin.site.register(Fruta)
admin.site.register(Legume)
admin.site.register(Verdura)
admin.site.register(Bebida)
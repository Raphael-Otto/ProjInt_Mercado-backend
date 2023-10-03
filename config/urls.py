from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from mercado.views import CategoriaViewSet, MarcaViewSet, CarneViewSet, LaticínioViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"carnes", CarneViewSet)
router.register(r"laticinios", LaticínioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
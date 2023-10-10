from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView)

from mercado.views import CategoriaViewSet, MarcaViewSet, CarneViewSet, LaticínioViewSet, FrutaViewSet, LegumeViewSet, VerduraViewSet, BebidaViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"carnes", CarneViewSet)
router.register(r"laticinios", LaticínioViewSet)
router.register(r"frutas", FrutaViewSet)
router.register(r"legumes", LegumeViewSet)
router.register(r"verduras", VerduraViewSet)
router.register(r"bebidas", BebidaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
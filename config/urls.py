from django.contrib import admin
from django.urls import include, path
from usuario.router import router as usuario_router
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView)
from uploader.router import router as uploader_router

from mercado.views.categoria import CategoriaViewSet;   
from mercado.views.marca import MarcaViewSet;
from mercado.views.carne import CarneViewSet;
from mercado.views.laticinio import LaticínioViewSet;
from mercado.views.fruta import FrutaViewSet;
from mercado.views.legume import LegumeViewSet;
from mercado.views.verdura import VerduraViewSet;
from mercado.views.bebida import BebidaViewSet;

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
    path("api/", include(usuario_router.urls)),
    path("api/media/", include(uploader_router.urls)),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
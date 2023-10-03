from rest_framework.viewsets import ModelViewSet

from mercado.models import Categoria, Marca
from mercado.serializers import CategoriaSerializer, MarcaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
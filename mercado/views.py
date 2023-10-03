from rest_framework.viewsets import ModelViewSet

from mercado.models import Categoria, Marca, Carne, Laticínio
from mercado.serializers import CategoriaSerializer, MarcaSerializer, CarneSerializer, LaticínioSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class CarneViewSet(ModelViewSet):
    queryset = Carne.objects.all()
    serializer_class = CarneSerializer

class LaticínioViewSet(ModelViewSet):
    queryset = Laticínio.objects.all()
    serializer_class = LaticínioSerializer
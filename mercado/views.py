from rest_framework.viewsets import ModelViewSet

from mercado.models import Categoria, Marca, Carne, Laticínio, Fruta, Legume, Verdura
from mercado.serializers import CategoriaSerializer, MarcaSerializer, CarneSerializer, LaticínioSerializer, FrutaSerializer, LegumeSerializer, VerduraSerializer

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
    
class FrutaViewSet(ModelViewSet):
    queryset = Fruta.objects.all()
    serializer_class = FrutaSerializer
    
class LegumeViewSet(ModelViewSet):
    queryset = Legume.objects.all()
    serializer_class = LegumeSerializer
    
class VerduraViewSet(ModelViewSet):
    queryset = Verdura.objects.all()
    serializer_class = VerduraSerializer
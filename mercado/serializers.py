from rest_framework.serializers import ModelSerializer

from mercado.models import Categoria, Marca, Carne, Laticínio

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class CarneSerializer(ModelSerializer):
    class Meta:
        model = Carne
        fields = "__all__"
        depth = 1

class LaticínioSerializer(ModelSerializer):
    class Meta:
        model = Laticínio
        fields = "__all__"
        depth = 1
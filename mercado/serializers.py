from rest_framework.serializers import ModelSerializer

from mercado.models import Categoria, Marca, Carne, Laticínio, Fruta, Legume, Verdura

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
        
class FrutaSerializer(ModelSerializer):
    class Meta:
        model = Fruta
        fields = "__all__"
        depth = 1
        
class LegumeSerializer(ModelSerializer):
    class Meta:
        model = Legume
        fields = "__all__"
        depth = 1
        
class VerduraSerializer(ModelSerializer):
    class Meta:
        model = Verdura
        fields = "__all__"
        depth = 1
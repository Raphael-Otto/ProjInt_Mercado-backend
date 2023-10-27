from django.db import models

from rest_framework.serializers import ModelSerializer, SlugRelatedField
from mercado.models import Marca

from uploader.models import Image
from uploader.serializers import ImageSerializer

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"
    
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
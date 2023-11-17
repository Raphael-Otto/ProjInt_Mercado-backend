from django.db import models

from rest_framework.serializers import ModelSerializer
from mercado.models import Bebida

from uploader.models import Image
from uploader.serializers import ImageSerializer

class BebidaSerializer(ModelSerializer):
    class Meta:
        model = Bebida
        fields = "__all__"
        depth = 1
        
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
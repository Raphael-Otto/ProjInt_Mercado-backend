from django.db import models

from rest_framework.serializers import ModelSerializer
from mercado.models import Fruta

class FrutaSerializer(ModelSerializer):
    class Meta:
        model = Fruta
        fields = "__all__"
        depth = 1
        
from django.db import models

from rest_framework.serializers import ModelSerializer
from mercado.models import Verdura

class VerduraSerializer(ModelSerializer):
    class Meta:
        model = Verdura
        fields = "__all__"
        depth = 1
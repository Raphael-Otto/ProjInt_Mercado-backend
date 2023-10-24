from django.db import models

from rest_framework.serializers import ModelSerializer
from mercado.models import Legume
   
class LegumeSerializer(ModelSerializer):
    class Meta:
        model = Legume
        fields = "__all__"
        depth = 1
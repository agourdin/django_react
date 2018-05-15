from rest_framework import serializers
from . import models

class ModelExampleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.ModelExample

from django.shortcuts import render

from rest_framework import generics

from . import models
from . import serializers

class ListModelExample(generics.ListCreateAPIView):
    queryset = models.ModelExample.objects.all()
    serializer_class = serializers.ModelExampleSerializer


class DetailModelExample(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ModelExample.objects.all()
    serializer_class = serializers.ModelExampleSerializer

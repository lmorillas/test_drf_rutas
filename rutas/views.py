from django.shortcuts import render

# Create your views here.

from .models import Archivo
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import ArchivoSerializer
import uuid


class ArchivoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Archivo.objects.all().order_by('ruta')
    serializer_class = ArchivoSerializer

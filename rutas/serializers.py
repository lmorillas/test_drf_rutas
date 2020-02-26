from .models import Archivo
import uuid
from rest_framework import serializers
class ArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivo
        fields = ['ruta', 'rutaid']
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        ruta = validated_data.get('ruta')
        rutaid = uuid.uuid4()
        return Archivo.objects.create(**validated_data, rutaid=rutaid)
from rest_framework import serializers, viewsets

from Access.api.simple_serializers import SimpleUsuarioSerializer
from Access.models import MetodoPago


class MetodoPagoSerializer(serializers.ModelSerializer):
    usuario_data = SimpleUsuarioSerializer(read_only=True, required=False, source='usuario')

    class Meta:
        model = MetodoPago
        fields = '__all__'


class MetodoPagoViewSet(viewsets.ModelViewSet):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer

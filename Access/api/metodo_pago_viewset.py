from rest_framework import serializers, viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

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

    def create(self, request, *args, **kwargs):
        # Comprobar permisos
        response = self.check_permissions(request)
        if response:
            return response

        # Serializar datos de la solicitud
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Crear instancia temporal del método de pago para validar
        metodo_pago_data = serializer.validated_data
        metodo_pago = MetodoPago(
            usuario=request.user,
            nombre_titular=metodo_pago_data['nombre_titular'],
            numero_tarjeta=metodo_pago_data['numero_tarjeta'],
            fecha_expiracion=metodo_pago_data['fecha_expiracion'],
            cvv=metodo_pago_data['cvv'],
        )

        # Verificar validez de la tarjeta
        if not metodo_pago.verify_validez_tarjeta():
            raise ValidationError({'detail': 'La tarjeta proporcionada no es válida o no es Visa.'})

        # Confirmar que es Visa
        if not metodo_pago.numero_tarjeta.startswith('4'):
            raise ValidationError({'detail': 'Solo se aceptan tarjetas Visa.'})

        # Guardar el método de pago si pasa las validaciones
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

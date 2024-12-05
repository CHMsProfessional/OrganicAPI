from rest_framework import serializers, viewsets, status
from rest_framework.response import Response

from Access.api import SimpleEmpresaSerializer
from Access.models import SuscripcionEmpresa


class SuscripcionEmpresaSerializer(serializers.ModelSerializer):
    empresas_data = SimpleEmpresaSerializer(read_only=True, source='empresas')

    class Meta:
        model = SuscripcionEmpresa
        fields = '__all__'


class SuscripcionEmpresaViewSet(viewsets.ModelViewSet):
    queryset = SuscripcionEmpresa.objects.all()
    serializer_class = SuscripcionEmpresaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.imagen:
            import os
            if os.path.exists(instance.imagen.path):
                os.remove(instance.imagen.path)

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        current_image_path = instance.imagen.path if instance.imagen else None

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        new_image = request.FILES.get('imagen', None)

        if new_image:
            if current_image_path:
                import os
                if os.path.exists(current_image_path):
                    os.remove(current_image_path)

            instance.imagen = new_image

        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data, status=status.HTTP_200_OK)

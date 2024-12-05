# Generated by Django 5.0.4 on 2024-12-03 04:04

import Access.models.Empresa
import Access.models.Producto
import Access.models.SuscripcionEmpresa
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Access', '0008_alter_compra_fecha_validez_alter_empresa_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='fecha_validez',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=Access.models.Empresa.unique_image_path),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=Access.models.Producto.unique_image_path),
        ),
        migrations.AlterField(
            model_name='suscripcionempresa',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=Access.models.SuscripcionEmpresa.unique_image_path),
        ),
    ]

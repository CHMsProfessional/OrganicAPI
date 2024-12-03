# Generated by Django 5.0.4 on 2024-12-03 04:06

import Access.models.Empresa
import Access.models.Producto
import Access.models.SuscripcionEmpresa
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Access', '0009_alter_compra_fecha_validez_alter_empresa_imagen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='fecha_validez',
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
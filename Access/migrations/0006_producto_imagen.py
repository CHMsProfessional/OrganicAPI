# Generated by Django 5.0.4 on 2024-12-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Access', '0005_newsletter_alter_compra_costo_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]
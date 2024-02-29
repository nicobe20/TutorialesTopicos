# Generated by Django 4.2.5 on 2024-02-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('usuario', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15)),
                ('historial_compras', models.TextField()),
                ('opiniones', models.TextField()),
            ],
        ),
    ]
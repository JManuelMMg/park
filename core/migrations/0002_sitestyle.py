# Generated by Django 5.2.1 on 2025-06-02 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_color', models.CharField(default='#2c3e50', max_length=7, verbose_name='Color Primario')),
                ('secondary_color', models.CharField(default='#3498db', max_length=7, verbose_name='Color Secundario')),
                ('accent_color', models.CharField(default='#e74c3c', max_length=7, verbose_name='Color de Acento')),
                ('background_color', models.CharField(default='#f8f9fa', max_length=7, verbose_name='Color de Fondo')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='branding/', verbose_name='Logo')),
                ('theme', models.CharField(choices=[('light', 'Claro'), ('dark', 'Oscuro'), ('corporate', 'Corporativo')], default='light', max_length=20, verbose_name='Tema')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('font_family', models.CharField(choices=[('Segoe UI', 'Segoe UI'), ('Roboto', 'Roboto'), ('Montserrat', 'Montserrat'), ('Arial', 'Arial'), ('Verdana', 'Verdana')], default='Segoe UI', max_length=50, verbose_name='Fuente Principal')),
                ('border_radius', models.CharField(default='8px', max_length=10, verbose_name='Radio de Bordes')),
                ('base_font_size', models.CharField(default='16px', max_length=10, verbose_name='Tamaño de Fuente Base')),
                ('layout', models.CharField(choices=[('fixed', 'Ancho Fijo'), ('fluid', 'Ancho Fluido')], default='fluid', max_length=20, verbose_name='Layout')),
            ],
            options={
                'verbose_name': 'Estilo del Sitio',
                'verbose_name_plural': 'Estilos del Sitio',
            },
        ),
    ]

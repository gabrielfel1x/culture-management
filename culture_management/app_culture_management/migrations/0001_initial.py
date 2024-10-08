# Generated by Django 5.1 on 2024-08-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('show', 'Show musical'), ('teatro', 'Apresentação teatral'), ('orquestra', 'Orquestra'), ('musical', 'Musical'), ('humor', 'Show de humor')], max_length=50)),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('local', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=100)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('entrada_gratuita', models.BooleanField(default=False)),
                ('vagas', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]

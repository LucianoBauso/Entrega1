# Generated by Django 4.1.1 on 2022-09-20 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrantes', '0002_casa_primito'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=7)),
                ('modelo', models.CharField(max_length=15)),
                ('anio', models.IntegerField()),
                ('color', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Primito',
        ),
    ]

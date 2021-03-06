# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-14 13:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Contactos', '0002_auto_20161228_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObraSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Obra Social',
                'verbose_name_plural': 'Obras Sociales',
            },
        ),
        migrations.AlterModelOptions(
            name='contactos',
            options={'verbose_name': 'Contacto', 'verbose_name_plural': 'Contactos'},
        ),
        migrations.AddField(
            model_name='contactos',
            name='NroAfiliado',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='contactos',
            name='Nombre',
            field=models.CharField(max_length=120),
        ),
        migrations.AddField(
            model_name='contactos',
            name='ObraSocial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Contactos.ObraSocial'),
        ),
    ]

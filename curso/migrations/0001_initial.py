# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-14 02:16
from __future__ import unicode_literals

import curso.models
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.FileField(upload_to=curso.models.Arquivos.get_upload_to)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Arquivo',
                'verbose_name_plural': 'Arquivos',
            },
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to=curso.models.Foto.get_upload_to)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Album',
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=90, verbose_name='Titulo')),
                ('descricao', djangocms_text_ckeditor.fields.HTMLField(blank=True, null=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Matéria',
                'verbose_name_plural': 'Matérias',
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('slug', models.CharField(max_length=30, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Album',
            },
        ),
        migrations.AddField(
            model_name='materia',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materias', to='curso.Periodo'),
        ),
    ]

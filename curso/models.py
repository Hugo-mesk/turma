from django.utils.translation import ugettext_lazy as _
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
import os

# Create your models here.
class Arquivos(models.Model):
    def get_upload_to(self, filename):
        filePath = (self.content_object.titulo)
        if filename.replace(" ", "_"):
            filename = filename.replace(" ", "_")

        if filePath.replace(" ", "_"):
            filePath = filePath.replace(" ", "_")

        return os.path.join(filePath,filename)

    documento = models.FileField(upload_to=get_upload_to)
    data_criacao = models.DateField(auto_now_add=True)
    # Tecnica de foreing key generica
    # Em vez de declara a chave estrageira nessa classe vamos torna-la disponivel para todas as classes
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.documento.name

    class Meta:
        verbose_name = _("Arquivo")
        verbose_name_plural = _("Arquivos")

class Foto(models.Model):
    def get_upload_to(self, filename):
        filePath = self.content_object.titulo
        if filename.replace(" ", "_"):
            filePath = os.path.join(filePath , (filename.replace(" ", "_"),))

        return filePath

    imagem = models.ImageField(upload_to=get_upload_to)
    data_criacao = models.DateField(auto_now_add=True)
    # Tecnica de foreing key generica
    # Em vez de declara a chave estrageira nessa classe vamos torna-la disponivel para todas as classes
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.imagem.name

    class Meta:
        verbose_name = _("Foto")
        verbose_name_plural = _("Album")


class Periodo(models.Model):
    numero = models.IntergerField(verbose_name = _('Número'))
    slug = models.CharField(verbose_name = _('Slug'),
                            max_length=30)

    def __str__(self):
        return self.imagem.name

    class Meta:
        verbose_name = _("Foto")
        verbose_name_plural = _("Album")


class Materia(models.Model):
    titulo = models.CharField(verbose_name=_('Titulo'),
                              max_length=90)
    descricao = HTMLField(verbose_name=_('Descrição'),
                            configuration='CKEDITOR_SETTINGS',
                            null=True,
                            blank=True)
    periodo = models.ForeignKey(Periodo,'Matérias')
    # Como indicado acima usamos aqui as chaves estrageiras genericas
    arquivos = GenericRelation(Arquivos, verbose_name=_("arquivos"))
    album = GenericRelation(Foto, verbose_name=_("Album"))

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = _("Matéria")
        verbose_name_plural = _("Matérias")

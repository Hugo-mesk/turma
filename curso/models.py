from django.utils.translation import ugettext_lazy as _
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
import os
from django.db.models import Count

# Create your models here.
class Arquivos(models.Model):
    def get_upload_to(self, filename):
        materiaPath = self.content_object.slug
        priodoPath = self.content_object.periodo.slug
        myPath = os.path.join(priodoPath,materiaPath)
        if filename.replace(" ", "_"):
            filename = "{}".format(filename.replace(" ", "_"))
        else:
            filename = "{}".format(filename)

        return os.path.join(myPath,filename)

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
        materiaPath = self.content_object.slug
        priodoPath = self.content_object.periodo.slug
        myPath = os.path.join(priodoPath,materiaPath)
        if filename.replace(" ", "_"):
            filename = "{}".format(filename.replace(" ", "_"))
        else:
            filename = "{}".format(filename)

        return os.path.join(myPath,filename)

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
    numero = models.IntegerField(verbose_name = _('Número'))
    titulo = models.CharField(verbose_name=_('Titulo'),
                              max_length=90)
    slug = models.SlugField(verbose_name = _('Slug'),
                            max_length=30)

    def __str__(self):
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        return ('curso:periodo-detail', (), {'periodo_slug': self.slug})

    class Meta:
        verbose_name = _("Periodo")
        verbose_name_plural = _("Periodos")


class Materia(models.Model):
    titulo = models.CharField(verbose_name=_('Titulo'),
                              max_length=90)
    slug = models.SlugField(verbose_name = _('Slug'),
                            max_length=30)
    descricao = HTMLField(verbose_name=_('Descrição'),
                            configuration='CKEDITOR_SETTINGS',
                            null=True,
                            blank=True)
    periodo = models.ForeignKey(Periodo,
                                on_delete=models.CASCADE,
                                related_name='materias')
    # Como indicado acima usamos aqui as chaves estrageiras genericas
    arquivos = GenericRelation(Arquivos, verbose_name=_("arquivos"))
    album = GenericRelation(Foto, verbose_name=_("Album"))

    def __str__(self):
        return self.titulo

    @property
    def group(self):
        periodo = Periodo.objects.prefetch_related('materias').filter(pk=self.periodo.pk).annotate(num_materias=Count('materias'))
        print(periodo[0])
        return periodo[0].num_materias//4

    @models.permalink
    def get_absolute_url(self):
        return ('curso:materia', (), {'periodo_slug':self.periodo.slug,'materia_slug':self.slug})

    class Meta:
        verbose_name = _("Matéria")
        verbose_name_plural = _("Matérias")

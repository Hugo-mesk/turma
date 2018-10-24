from django.utils.translation import ugettext_lazy as _
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Arquivos(models.Model):
    def get_upload_to(self, filename):
        filePath = (self.content_object.title)
        if filename.replace(" ", "_"):
            filePath = filePath.replace(" ", "_") + (filename.replace(" ", "_"),)

        return os.path.join(*(filePath))

    documento = models.FileField(upload_to=get_upload_to)
    data_criacao = models.DateField(auto_now_add=True)
    # Tecnica de foreing key generica
    # Em vez de declara a chave estrageira nessa classe vamos torna-la disponivel para todas as classes
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    objeto_do_conteudo = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.document.name

    class Meta:
        verbose_name = _("Material")
        verbose_name_plural = _("Materiais")

class Foto(models.Model):
    def get_upload_to(self, filename):
        filePath = self.content_object.title
        if filename.replace(" ", "_"):
            filePath = os.path.join(filePath , (filename.replace(" ", "_"),))

        return filePath

    imagem = models.ImageField(upload_to=get_upload_to)
    data_criacao = models.DateField(auto_now_add=True)
    # Tecnica de foreing key generica
    # Em vez de declara a chave estrageira nessa classe vamos torna-la disponivel para todas as classes
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    objeto_do_conteudo = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.document.name

    class Meta:
        verbose_name = _("Foto")
        verbose_name_plural = _("Album")


class Assunto(models.Model):
    titulo = models.CharField(verbose_name=_('Titulo'),
                              max_length=90)
    descricao = HTMLField(verbose_name=_('Descrição'),
                            configuration='CKEDITOR_SETTINGS',
                            null=True,
                            blank=True)
    # Como indicado acima usamos aqui as chaves estrageiras genericas
    materiais = GenericRelation(Arquivos, verbose_name=_("Materials"))
    album = GenericRelation(Foto, verbose_name=_("Album"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Assunto")
        verbose_name_plural = _("Assuntos")

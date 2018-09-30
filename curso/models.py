from django.utils.translation import ugettext_lazy as _
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Material(models.Model):
    def get_upload_to(self, filename):
        filePath = (self.content_object.title)
        if filename.replace(" ", "_"):
            filePath = filePath + (filename.replace(" ", "_"),)

        return os.path.join(*(filePath))

    document = models.FileField(upload_to=get_upload_to)
    creation_date = models.DateField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.document.name

    class Meta:
        verbose_name = _("Material")
        verbose_name_plural = _("Materials")

class Photograph(models.Model):
    def get_upload_to(self, filename):
        filePath = (self.content_object.title)
        if filename.replace(" ", "_"):
            filePath = filePath + (filename.replace(" ", "_"),)

        return os.path.join(*(filePath))

    document = models.ImageField(upload_to=get_upload_to)
    creation_date = models.DateField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.document.name

    class Meta:
        verbose_name = _("Photograph")
        verbose_name_plural = _("Album")


class Subject(models.Model):
    title = models.CharField(verbose_name=_('Title'),
                              max_length=90)
    description = HTMLField(verbose_name=_('Description'),
                            configuration='CKEDITOR_SETTINGS',
                            null=True,
                            blank=True)
    materials = GenericRelation(Material, verbose_name=_("Materials"))
    album = GenericRelation(Photograph, verbose_name=_("Album"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

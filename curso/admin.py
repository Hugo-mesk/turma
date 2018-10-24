from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline
from .models import Arquivos, Foto, Assunto


# Register your models here.
class ArquivosInline(GenericTabularInline):
    model = Arquivos
    extra = 0


class FotoInline(GenericStackedInline):
    model = Foto
    extra = 0


class AssuntoAdmin(admin.ModelAdmin):
    inlines = [
               ArquivosInline,
               FotoInline,
              ]


admin.site.register(Foto)
admin.site.register(Arquivos)
admin.site.register(Assunto, AssuntoAdmin)
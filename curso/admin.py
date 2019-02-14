from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline
from .models import Arquivos, Foto, Materia, Periodo


# Register your models here.
class ArquivosInline(GenericTabularInline):
    model = Arquivos
    extra = 0


class FotoInline(GenericStackedInline):
    model = Foto
    extra = 0


class MateriaAdmin(admin.ModelAdmin):
    inlines = [
               ArquivosInline,
               FotoInline,
              ]


admin.site.register(Periodo)
admin.site.register(Foto)
admin.site.register(Arquivos)
admin.site.register(Materia, MateriaAdmin)

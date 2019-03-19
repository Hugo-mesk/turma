from django.contrib import admin
from .models import Arquivo, Foto, Materia, Periodo


class FotoInline(admin.TabularInline):
    model = Foto


class ArquivoInline(admin.TabularInline):
    model = Arquivo


class MateriaAdmin(admin.ModelAdmin):
    inlines = [
        FotoInline,
        ArquivoInline,
    ]

admin.site.register(Periodo)
admin.site.register(Foto)
admin.site.register(Arquivo)
admin.site.register(Materia, MateriaAdmin)

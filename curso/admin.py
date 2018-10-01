from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline
from .models import Subject, Photograph, Material


# Register your models here.
class MaterialInline(GenericTabularInline):
    model = Material
    extra = 0


class PhotographInline(GenericStackedInline):
    model = Photograph
    extra = 0


class SubjectAdmin(admin.ModelAdmin):
    inlines = [
               MaterialInline,
               PhotographInline,
              ]


admin.site.register(Photograph)
admin.site.register(Material)
admin.site.register(Subject, SubjectAdmin)
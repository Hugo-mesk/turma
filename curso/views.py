from django.shortcuts import get_object_or_404
from .models import Materia, Periodo, Arquivos, Foto
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView
from extra_views.generic import GenericInlineFormSetFactory


class PeriodoInline(InlineFormSetFactory):
    model = Periodo


class ArquivosInline(GenericInlineFormSetFactory):
    model = Arquivos
    fields = ['documento']
    factory_kwargs = {'ct_field': 'content_type', 'fk_field': 'object_id',
                      'extra': 1}
    formset_kwargs = {'save_as_new': True}


class FotoInline(GenericInlineFormSetFactory):
    model = Foto
    fields = ['imagem']
    factory_kwargs = {'ct_field': 'content_type', 'fk_field': 'object_id',
                      'extra': 1}
    formset_kwargs = {'save_as_new': True}

class MateriaCreateView(CreateWithInlinesView):
    model = Materia
    inlines = [ArquivosInline, FotoInline]
    fields = "__all__"
    template_name = 'curso/materia_criar.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


# class OrderUpdateView(UpdateWithInlinesView):
#     model = Order
#     form_class = OrderForm
#     inlines = [ItemsInline, TagsInline]
#
#     def get_success_url(self):
#         return self.object.get_absolute_url()

# class MateriaCreateView(CreateView):
#     model = Materia
#     fields = ['titulo', 'slug', 'descricao', 'periodo', 'arquivos', 'album']
#     template = 'curso/materia_criar.html'


@login_required
def CursoListView(request):
    periodos = Periodo.objects.order_by('numero').prefetch_related('materias')

    template = loader.get_template('curso/materias.html')

    context = {
        'periodos': periodos,
    }
    return HttpResponse(template.render(context, request))


@login_required
def PeriodoDetailView(request, periodo_slug):
    periodo = get_object_or_404(Periodo.objects.filter(slug=periodo_slug).prefetch_related('materias'))
    materias = periodo.materias.all()

    template = loader.get_template('curso/periodo.html')

    context = {
        'periodo': periodo,
        'materias': materias,
    }
    return HttpResponse(template.render(context, request))


@login_required
def MateriaDetailView(request, periodo_slug, materia_slug):
    materia = get_object_or_404(Materia.objects.filter(periodo__slug=periodo_slug, slug=materia_slug))
    arquivos = materia.arquivos.all()
    album = materia.album.all()

    template = loader.get_template('curso/materia.html')

    context = {
        'materia': materia,
        'arquivos': arquivos,
        'album': album,
    }
    return HttpResponse(template.render(context, request))

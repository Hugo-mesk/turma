from django.shortcuts import get_object_or_404
from .models import Materia, Periodo, Arquivos, Foto
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView
from extra_views.generic import GenericInlineFormSetFactory


class ArquivosInline(GenericInlineFormSetFactory):
    model = Arquivos
    fields = "__all__"
    factory_kwargs = {'ct_field': 'content_type', 'fk_field': 'object_id',
                      'extra': 1}


class FotoInline(GenericInlineFormSetFactory):
    model = Foto
    fields = "__all__"
    factory_kwargs = {'ct_field': 'content_type', 'fk_field': 'object_id',
                      'extra': 1}



class MateriaCreateView(CreateWithInlinesView):
    model = Materia
    inlines = [ArquivosInline, FotoInline]
    fields = "__all__"
    template_name = 'curso/materia_criar.html'

    def get_success_url(self):
        return self.object.get_absolute_url()

class MaterialUpdateView(UpdateWithInlinesView):
    model = Materia
    inlines = [ArquivosInline, FotoInline]
    fields = "__all__"
    slug_url_kwarg = 'materia_slug'
    template_name = 'curso/materia_atualizar.html'

    def get_success_url(self):
       return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        materia = get_object_or_404(Materia.objects.filter(slug=kwargs['materia_slug']))
        context['materia'] = materia
        context['arquivos'] = materia.arquivos.all()
        context['album'] = materia.album.all()
        return context


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

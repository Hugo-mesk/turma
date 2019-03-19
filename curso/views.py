from django.shortcuts import get_object_or_404
from .models import Materia, Periodo, Arquivo, Foto
from .forms import FotoForm, ArquivoForm
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views import View

#from django.urls import reverse

from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.contenttypes.forms import  generic_inlineformset_factory


#https://stackoverflow.com/questions/16931901/django-combine-detailview-and-formview
#https://stackoverflow.com/questions/4497684/django-class-based-views-with-inline-model-form-or-formset


class MateriaDisplay(DetailView):
    model = Materia
    fields = "__all__"
    template_name = 'curso/materia_atualizar.html'
    slug_url_kwarg = 'materia_slug'

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        materia = self.object
        arquivos = Arquivo.objects.filter(materia=self.object)
        album = Foto.objects.filter(materia=self.object)
        context['materia'] = materia
        context['album'] = album
        context['arquivos'] = arquivos
        # Create a formset instance to edit an existing model object,
        # but use POST data to populate the formset.
        context['foto_form'] = FotoForm()
        context['arquivo_form'] = ArquivoForm()

        return context


class FotoCreate(CreateView):
    model= Foto
    form_class = FotoForm
    http_method_names = ['post']

    def get_success_url(self):
        materia = Materia.objects.get(slug=self.kwargs['materia_slug'])
        return materia.get_absolute_url()

    def form_valid(self, form):
        materia = Materia.objects.get(slug=self.kwargs['materia_slug'])
        form.instance.materia = materia
        return super().form_valid(form)



class ArquivoCreate(CreateView):
    model= Arquivo
    form_class = ArquivoForm
    http_method_names = ['post']

    def get_success_url(self):
        materia = Materia.objects.get(slug=self.kwargs['materia_slug'])
        return materia.get_absolute_url()

    def form_valid(self, form):
        materia = Materia.objects.get(slug=self.kwargs['materia_slug'])
        form.instance.materia = materia
        return super().form_valid(form)



class MateriaDetailView(View):
    def get(self, request, *args, **kwargs):
        view = MateriaDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'arquivo_submit' in request.POST:
            view = ArquivoCreate.as_view()
            return view(request, *args, **kwargs)

        if 'foto_submit' in request.POST:
            view = FotoCreate.as_view()
            return view(request, *args, **kwargs)


class MateriaCreateView(CreateView):
    model = Materia
    fields = "__all__"
    template_name = 'curso/materia_criar.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


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


#@login_required
#def MateriaDetailView(request, periodo_slug, materia_slug):
#    materia = get_object_or_404(Materia.objects.filter(periodo__slug=periodo_slug, slug=materia_slug))
#    arquivos = materia.arquivos.all()
#    album = materia.album.all()
#
#    template = loader.get_template('curso/materia.html')
#
#    context = {
#        'materia': materia,
#        'arquivos': arquivos,
#        'album': album,
#    }
#    return HttpResponse(template.render(context, request))

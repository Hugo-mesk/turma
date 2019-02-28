from django.shortcuts import get_object_or_404
from .models import Materia, Periodo, Arquivos, Foto
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
#from django.urls import reverse

from django.views.generic import CreateView, UpdateView #, DetailView
from django.contrib.contenttypes.forms import  generic_inlineformset_factory


#https://stackoverflow.com/questions/16931901/django-combine-detailview-and-formview
#https://stackoverflow.com/questions/4497684/django-class-based-views-with-inline-model-form-or-formset

class MateriaView (UpdateView):
    model = Materia
    template_name = 'curso/materia_atualizar.html'
    slug_url_kwarg = 'materia_slug'
    context_object_name = 'form'
    fields = "__all__"
    success_url = self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        materia = Materia.objects.get(periodo__slug=self.object.periodo.slug, slug=self.object.slug)
        arquivos = materia.arquivos.all()
        album = materia.album.all()
        context['materia'] = materia
        context['album'] = album
        context['arquivos'] = arquivos
        context['named_formset'] = self.get_named_formsets()

        return context

    def get_named_formsets(self):
        FotoFormSet = generic_inlineformset_factory(Foto,extra=1,can_delete=False)
        DocumentoFormSet = generic_inlineformset_factory(Arquivos,extra=1,can_delete=False)

        return {
            'foto_formset': FotoFormSet(self.request.POST or None, self.request.FILES or None),
            'arquivo_formset': DocumentoFormSet(self.request.POST or None, self.request.FILES or None),
               }

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        #self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, '{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return self.object.get_absolute_url()

    def foto_formset_valid(self, formset):
        """
        Hook for custom formset saving.. useful if you have multiple formsets
        """
        fotos = formset.save(commit=False) # self.save_formset(formset, contact)
        for foto in fotos:
            foto.content_object = self.request.materia
            foto.save()

    def arquivo_formset_valid(self, formset):
        """
        Hook for custom formset saving.. useful if you have multiple formsets
        """
        arquivos = formset.save(commit=False) # self.save_formset(formset, contact)
        for arquivo in arquivos:
            arquivo.content_object = self.request.materia
            arquivo.save()

    def get_success_url(self):
        return self.object.get_absolute_url()

class MateriaCreateView(CreateView):
    model = Materia
    fields = "__all__"
    template_name = 'curso/materia_criar.html'

    def get_success_url(self):
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        FotoFormSet = generic_inlineformset_factory(Foto,extra=1)
        DocumentoFormSet = generic_inlineformset_factory(Arquivos,extra=1)

        if self.request.POST:
            # Create a formset instance to edit an existing model object,
            # but use POST data to populate the formset.
            context['foto_formset'] = FotoFormSet(self.request.POST, instance=self.get_object())
            context['documento_formset'] = DocumentoFormSet(self.request.POST, instance=self.get_object())
        else:
            # Create a formset with the data from model object and add it to context
            context['foto_formset'] = FotoFormSet(instance=self.get_object())
            context['documento_formset'] = DocumentoFormSet(instance=self.get_object())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        fotos_form = context['foto_formset']
        documentos_forms = context['documento_formset']
        if fotos_form.is_valid() and documentos_forms.is_valid():
            self.object = form.save()
            fotos_form.instance = self.object
            fotos_form.save()
            documentos_forms.instance = self.object
            documentos_forms.save()
            return self.object.get_absolute_url()
        else:
            return self.render_to_response(self.get_context_data(form=form))


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
#   album = materia.album.all()
#
#    template = loader.get_template('curso/materia.html')
#
#    context = {
#        'materia': materia,
#        'arquivos': arquivos,
#        'album': album,
#    }
#    return HttpResponse(template.render(context, request))

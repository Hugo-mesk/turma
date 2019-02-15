from django.shortcuts import get_object_or_404
from .models import Materia, Periodo
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required



@login_required
def lista_materias(request):
    periodos = Periodo.objects.order_by('numero').prefetch_related('materias')

    template = loader.get_template('curso/materias.html')

    context = {
        'periodos': periodos,
    }
    return HttpResponse(template.render(context, request))


@login_required
def periodo_detail(request, periodo_slug):
    periodo = get_object_or_404(Periodo.objects.filter(slug=periodo_slug).prefetch_related('materias'))
    materias = periodo.materias.all()

    template = loader.get_template('curso/periodo.html')

    context = {
        'periodo': periodo,
        'materias': materias,
    }
    return HttpResponse(template.render(context, request))


@login_required
def materia(request, periodo_slug, materia_titulo):
    materia = get_object_or_404(Materia.objects.filter(periodo__slug=periodo_slug, titulo=materia_titulo))
    arquivos = materia.arquivos.all()
    album = materia.album.all()

    template = loader.get_template('curso/materia.html')

    context = {
        'materia': materia,
        'arquivos': arquivos,
        'album': album,
    }
    return HttpResponse(template.render(context, request))

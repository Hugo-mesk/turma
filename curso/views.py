from django.shortcuts import get_object_or_404
from .models import Assunto
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def subject_list(request):
    subject_list = Assunto.objects.order_by('id')

    template = loader.get_template('curso/subject.html')

    context = {
        'subject_list': subject_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def subject_detail(request, subject_id):
    subject = get_object_or_404(Assunto, pk=subject_id)
    lista_arquivos = subject.materiais.all()
    lista_fotos = subject.album.all()

    template = loader.get_template('curso/subject_detail.html')

    context = {
        'subject': subject,
        'lista_fotos': lista_fotos,
        'lista_arquivos': lista_arquivos,
    }
    return HttpResponse(template.render(context, request))
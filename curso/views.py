from django.shortcuts import get_object_or_404
from .models import Subject
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def subject_list(request):
    subject_list = Subject.objects.order_by('id')

    template = loader.get_template('curso/subject.html')

    context = {
        'subject_list': subject_list,
    }
    return HttpResponse(template.render(context, request))


@login_required
def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    photograph_list = subject.album.all()
    material_list = subject.materials.all()

    template = loader.get_template('curso/subject_detail.html')

    context = {
        'subject': subject,
        'photograph_list': photograph_list,
        'material_list': material_list,
    }
    return HttpResponse(template.render(context, request))
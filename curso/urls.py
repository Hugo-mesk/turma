from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /curso/
    url('^$', views.subject_list, name='materias'),
    # ex: /periodo/
    url('^(?P<periodo_slug>)/$', views.materia, name='materia'),
    # ex: /periodo/calculo
    url('^(?P<periodo_slug>)/(?P<materia_titulo>)/$', views.materia, name='materia'),
]
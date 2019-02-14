from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /periodo/calculo
    url('^(?P<periodo_slug>)/(?P<materia_titulo>)/$', views.materia, name='materia'),
    # ex: /periodo/
    url('^(?P<periodo_slug>)/$', views.periodo_detail, name='materia'),
    # ex: /curso/
    url('^$', views.lista_materias, name='materias'),
]

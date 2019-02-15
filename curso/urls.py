from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /periodo/calculo
    url('^(?P<periodo_slug>\w+)/(?P<materia_titulo>\w+)/$', views.materia, name='materia'),
    # ex: /periodo/
    url('^(?P<periodo_slug>\w+)/$', views.periodo_detail, name='materia'),
    # ex: /curso/
    url('^$', views.lista_materias, name='materias'),
]

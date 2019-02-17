from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /periodo/calculo
    url('^(?P<periodo_slug>[-\w]+)/(?P<materia_slug>[-\w]+)/$', views.MateriaDetailView, name='materia-detail'),
    # ex: /periodo/
    url('^(?P<periodo_slug>[-\w]+)/$', views.PeriodoDetailView, name='periodo-detail'),
    # ex: /curso/
    url('^$', views.CursoListView, name='curso_list'),
]

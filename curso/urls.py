from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /materia/criar
    url('materia/criar/$', views.MateriaCreateView.as_view(), name='materia-criar'),
    # ex: /materia/atualizar
    #url('materia/atualizar/(?P<materia_slug>[-\w]+)/$', views.MaterialUpdateView.as_view(), name='materia-atualizar'),
    # ex: /periodo/calculo
    url('(?P<periodo_slug>[-\w]+)/(?P<materia_slug>[-\w]+)/$', views.MateriaDetailView.as_view(), name='materia'),
    # ex: /periodo/
    url('(?P<periodo_slug>[-\w]+)/$', views.PeriodoDetailView, name='periodo-detail'),
    # ex: /foto/
    url('(?P<materia_slug>[-\w]+)/foto/$', views.FotoCreate.as_view(), name='foto'),
    # ex: /arquivo/
    url('(?P<materia_slug>[-\w]+)/arquivo/$', views.FotoCreate.as_view(), name='arquivo'),
    # ex: /curso/
    url('$', views.CursoListView, name='curso_list'),
]

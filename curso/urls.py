from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /materia/criar
    url('^materia/criar/$', views.MateriaCreateView.as_view(), name='materia-criar'),
    # ex: /materia/atualizar
    #url('^materia/atualizar/(?P<materia_slug>[-\w]+)/$', views.MaterialUpdateView.as_view(), name='materia-atualizar'),
    # ex: /periodo/calculo
    url('^(?P<periodo_slug>[-\w]+)/(?P<materia_slug>[-\w]+)/$', views.MateriaView.as_view(), name='materia'),
    # ex: /periodo/
    url('^(?P<periodo_slug>[-\w]+)/$', views.PeriodoDetailView, name='periodo-detail'),
    # ex: /curso/
    url('^$', views.CursoListView, name='curso_list'),
]

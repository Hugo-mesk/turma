from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /subject/
    url('^$', views.subject_list, name='subject_list'),
    # ex: /subject/5/
    url('^(?P<subject_id>[0-9]+)//$', views.subject_detail, name='subject_detail'),
]
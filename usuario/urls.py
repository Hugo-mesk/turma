# -*- coding: utf-8 *-*
from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^entrar/$', login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'index'}, name='logout'),
    url(r'^alterar-dados/$', views.update_user, name='update_user'),
    url(r'^alterar-senha/$', views.update_password, name='update_password'),
    url(r'^registro/$', views.register, name='register'),
]

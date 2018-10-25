from django.shortcuts import render
from django.views.generic import (
    CreateView, TemplateView, UpdateView, FormView
)
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import login as auth_login
from django.contrib.auth import get_user_model
from .forms import UserAdminCreationForm


User = get_user_model()

class IndexView(LoginRequiredMixin, TemplateView):

    template_name = 'registration/index.html'


class RegisterView(CreateView):

    model = User
    template_name = 'registration/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')


class UpdateUserView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'registration/update_user.html'
    fields = ['username', 'email']
    success_url = reverse_lazy('usuario:index')

    def get_object(self):
        return self.request.user


class UpdatePasswordView(LoginRequiredMixin, FormView):

    template_name = 'registration/update_password.html'
    success_url = reverse_lazy('usuario:index')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(UpdatePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(UpdatePasswordView, self).form_valid(form)


index = IndexView.as_view()
register = RegisterView.as_view()
update_user = UpdateUserView.as_view()
update_password = UpdatePasswordView.as_view()

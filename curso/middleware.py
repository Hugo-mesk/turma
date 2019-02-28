from django.http import HttpResponseRedirect

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

class LoginFormMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_request(self, request):
        from django.contrib.auth.forms import AuthenticationForm
        if request.method == 'POST' and request.POST.has_key('base-account') and request.POST['base-account'] == 'Login':
            form = AuthenticationForm(data=request.POST, prefix="login")
            if form.is_valid():
                from django.contrib.auth import login
                login(request, form.get_user())
            request.method = 'GET'
        else:
            form = AuthenticationForm(request, prefix="login")
        request.login_form = form
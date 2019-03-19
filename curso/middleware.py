from django.http import HttpResponseRedirect


class ArquivoFormMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(request, view_func, view_args, view_kwargs):
        from .forms import ArquivoForm
        context['arquivo_form'] =  ArquivoForm(request.POST, request.FILES)



class FotoFormMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(request, view_func, view_args, view_kwargs):
        from .forms import FotoForm
        context['foto_form'] = FotoForm(self.request.POST, self.request.FILES)



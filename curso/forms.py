from django.forms import ModelForm
from .models import Materia, Arquivo, Foto


class MateriaForm(ModelForm):
    class Meta:
        model = Materia
        fields = "__all__"


class ArquivoForm(ModelForm):
    class Meta:
        model = Arquivo
        fields = ['documento']


class FotoForm(ModelForm):
    class Meta:
        model = Foto
        fields = ['imagem']
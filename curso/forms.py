from django.forms import ModelForm
from .models import Materia, Arquivos, Foto

class MateriaForm(ModelForm):
    class Meta:
        model = Materia
        fields = "__all__"


class ArquivosForm(ModelForm):
    class Meta:
        model = Arquivos
        fields = "__all__"


class FotoForm(ModelForm):
    class Meta:
        model = Foto
        fields = "__all__"
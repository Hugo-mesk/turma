from django.forms import ModelForm
from .models import Periodo, Materia

class MateriaForm(ModelForm):
    class Meta:
        model = Materia
        fields = "__all__"

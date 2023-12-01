from django.forms import ModelForm
from equipos.models import Equipo

class EquiposForm(ModelForm):
    class Meta:
        model = Equipo
        fields = ['imei']

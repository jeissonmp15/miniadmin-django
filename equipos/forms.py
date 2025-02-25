from django.forms import ModelForm, fields

from equipos.models import Equipo


class EquiposForm(ModelForm):

    class Meta:
        model = Equipo
        fields = '__all__'

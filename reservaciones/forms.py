from django import forms
from .models import Huesped, Habitacion

class AsignacionForm(forms.ModelForm):

    class Meta:
        model = Grado
        fields = ('nombre', 'seccion','fechaH','materias')


def __init__ (self, *args, **kwargs):
        super(ReservacionForm, self).__init__(*args, **kwargs)
        self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["materias"].help_text = "Asignacion Exitosa"
        self.fields["materias"].queryset = Habitacion.objects.all()


class MateriaForm(forms.ModelForm):

    class Meta:
        model = Materia
        fields = ('nombre', 'creditos', 'fecha')

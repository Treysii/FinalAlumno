from django import forms
from .models import Huesped, Habitacion

class ReservacionForm(forms.ModelForm):

    class Meta:
        model = Huesped
        fields = ('nombre', 'apellido', 'telefono', 'direccion', 'fechaH','habitaciones')


def __init__ (self, *args, **kwargs):
        super(ReservacionForm, self).__init__(*args, **kwargs)
        self.fields["habitaciones"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["habitaciones"].help_text = "Reservacion Exitosa"
        self.fields["habitaciones"].queryset = Habitacion.objects.all()


class HabitacionForm(forms.ModelForm):

    class Meta:
        model = Habitacion
        fields = ('precio', 'piso', 'maxpersonas', 'camabb', 'bano', 'balcon', 'fecha')

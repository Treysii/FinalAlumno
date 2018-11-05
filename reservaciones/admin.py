from django.contrib import admin
from reservaciones.models import Habitacion, HabitacionAdmin, Huesped, HuespedAdmin

admin.site.register(Habitacion, HabitacionAdmin)
admin.site.register(Huesped, HuespedAdmin)
# Register your models here.

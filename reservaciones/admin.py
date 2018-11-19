from django.contrib import admin
from reservaciones.models import Materia, MateriaAdmin, Grado, GradoAdmin

admin.site.register(Materia, MateriaAdmin)
admin.site.register(Grado, GradoAdmin)
# Register your models here.

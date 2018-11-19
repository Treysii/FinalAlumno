from django.db import models
from django.contrib import admin
from django.utils import timezone
# Create your models here.

class Materia(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.IntegerField()
    fecha = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Grado(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    fechaH = models.DateField()
    materias = models.ManyToManyField(Materia, through='Asignacion')

    def __str__(self):
        return self.nombre

class Asignacion (models.Model):
    fecha_publicacions = models.DateTimeField(default=timezone.now)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

    def publish(self):
        self.fecha_publicacions = timezone.now()
        self.save()

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class MateriaAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class GradoAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

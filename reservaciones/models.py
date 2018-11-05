from django.db import models
from django.contrib import admin
from django.utils import timezone
# Create your models here.

class Habitacion(models.Model):
    precio = models.IntegerField()
    piso = models.IntegerField()
    maxpersonas = models.CharField(max_length=30)
    camabb = models.CharField(max_length=20)
    bano = models.CharField(max_length=15)
    balcon = models.CharField(max_length=15)
    fecha = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.maxpersonas

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

class Huesped(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=8)
    direccion = models.CharField(max_length=50)
    fecha_publicacion = models.DateTimeField(
                blank=True, null=True)
    habitaciones = models.ManyToManyField(Habitacion, through='Reserva')

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

class Reserva (models.Model):
    fecha_publicacions = models.DateTimeField(default=timezone.now)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    huesped = models.ForeignKey(Huesped, on_delete=models.CASCADE)

    def publish(self):
        self.fecha_publicacions = timezone.now()
        self.save()
class ReservaInLine(admin.TabularInline):
    model = Reserva
    extra = 1

class HabitacionAdmin(admin.ModelAdmin):
    inlines = (ReservaInLine,)

class HuespedAdmin(admin.ModelAdmin):
    inlines = (ReservaInLine,)

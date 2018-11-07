from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from .forms import ReservacionForm
from .forms import HabitacionForm
from django.urls import reverse
from reservaciones.models import Huesped, Reserva, Habitacion
from django.contrib.auth.decorators import login_required



def lista(request):
    pub =Reserva.objects.filter(fecha_publicacions__lte=timezone.now())
    return render(request, 'reservacion/listar.html', {'pub': pub})


def store(request):
    return render(request, 'reservacion/store.html')

def home(request):
    return render(request, 'reservacion/base.html')

def ver(request):
    return render(request, 'reservacion/ver.html')


def habitacion_nueva(request):
    if request.method == "POST":
        form = HabitacionForm(request.POST)
        if form.is_valid():
            hab = form.save(commit=False)
            hab.save()
            return redirect('lista_habitacion')
    else:
        form = HabitacionForm()
    return render(request, 'reservacion/habitacion_nuevo.html', {'form': form})

def lista_habitacion(request):
    habitacion = Habitacion.objects.order_by('id')
    return render(request, 'reservacion/listahab.html', {'habitacion':habitacion})





def habitacion_detalle(request, pk):
    habitaciones = get_object_or_404(Habitacion, pk=pk)
    return render(request, 'reservacion/detallehab.html', {'habitaciones': habitaciones})


def habitacion_editar(request, pk):
    habb = get_object_or_404(Habitacion, pk=pk)
    if request.method == "POST":
        form = HabitacionForm(request.POST, instance=habb)
        if form.is_valid():
            habb = form.save(commit=False)
            habb.save()
            return redirect('lista_habitacion')
    else:
        form = HabitacionForm(instance=habb)
    return render(request, 'reservacion/editarhab.html', {'form': form})

def habitacion_eliminar(request, pk):
    habit = get_object_or_404(Habitacion, pk=pk)
    habit.delete()
    return redirect('lista_habitacion')

@login_required
def reservacion_nueva(request):
    if request.method == "POST":
        formulario = ReservacionForm(request.POST)
        if formulario.is_valid():
            huesped = Huesped.objects.create(nombre=formulario.cleaned_data['nombre'], apellido = formulario.cleaned_data['apellido'], telefono= formulario.cleaned_data['telefono'], direccion = formulario.cleaned_data['direccion'], fechaH = formulario.cleaned_data['fechaH'])
            for habitacion_id in request.POST.getlist('habitaciones'):
                reservas = Reserva(habitacion_id=habitacion_id, huesped_id = huesped.id)
                reservas.save()
            messages.add_message(request, messages.SUCCESS, 'Reservacion Guardado Correctamente')
    else:
        formulario = ReservacionForm()
    return render(request, 'reservacion/hues_nuevo.html', {'formulario': formulario})

def huesped_editar(request, pk):
    huesped = get_object_or_404(Huesped, pk=pk)
    if request.method == "POST":
        form = ReservacionForm(request.POST, instance=huesped)
        if form.is_valid():
            huesped = form.save(commit=False)
            huesped.save()
            return redirect('lista_huesped')
    else:
        form = ReservacionForm(instance=huesped)
    return render(request, 'reservacion/huesped_editar.html', {'form': form})

def lista_huesped(request):
    huespeds  = Huesped.objects.order_by('fechaH')
    return render(request, 'reservacion/ver1.html', {'huespeds':huespeds})

def huesped_detalle(request, pk):
    huespedes = get_object_or_404(Huesped, pk=pk)
    return render(request, 'reservacion/detallehues.html', {'huespedes': huespedes})

def huesped_eliminar(request, pk):
    huesped = get_object_or_404(Huesped, pk=pk)
    huesped.delete()
    return redirect('lista_huesped')

from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone
from .forms import ReservacionForm
from .forms import HabitacionForm
from reservaciones.models import Huesped, Reserva, Habitacion
from django.contrib.auth.decorators import login_required

@login_required
def reservacion_nueva(request):
    if request.method == "POST":
        formulario = ReservacionForm(request.POST)
        if formulario.is_valid():
            huesped = Huesped.objects.create(nombre=formulario.cleaned_data['nombre'], apellido = formulario.cleaned_data['apellido'], telefono= formulario.cleaned_data['telefono'], direccion = formulario.cleaned_data['direccion'])
            for habitacion_id in request.POST.getlist('habitaciones'):
                reservas = Reserva(habitacion_id=habitacion_id, huesped_id = huesped.id)
                reservas.save()
            messages.add_message(request, messages.SUCCESS, 'Reservacion Guardado Correctamente')
    else:
        formulario = ReservacionForm()
    return render(request, 'reservacion/huesped_editar.html', {'formulario': formulario})


def lista(request):
    pub =Reserva.objects.filter(fecha_publicacions__lte=timezone.now())
    return render(request, 'reservacion/listar.html', {'pub': pub})
@login_required
def verlo(request):
    pubs =Reserva.objects.filter(fecha_publicacions__lte=timezone.now())
    return render(request, 'reservacion/ver1.html', {'pubs': pubs})

def store(request):
    return render(request, 'reservacion/store.html')

def home(request):
    return render(request, 'reservacion/base.html')

def ver(request):
    return render(request, 'reservacion/ver.html')


def editar(request):
    if request.method == "POST":
        formularios = ReservacionForm(request.POST)
        if formularios.is_valid():
            huesped = Huesped.objects.editar(nombre=formularios.cleaned_data['nombre'], apellido = formularios.cleaned_data['apellido'], telefono= formularios.cleaned_data['telefono'], direccion = formularios.cleaned_data['direccion'])
            for habitacion_id in request.POST.getlist('habitaciones'):
                reservas = Reserva(habitacion_id=habitacion_id, huesped_id = huesped.id)
                reservas.save()
            messages.add_message(request, messages.SUCCESS, 'Reservacion Guardado Correctamente')
    else:
        formularios = ReservacionForm()
    return render(request, 'reservacion/editar.html', {'formularios': formularios})

def borrador(request):
    draft = Reserva.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_publicacion')
    return render(request, 'reservacion/borrador.html', {'draft': draft})




def habitacion_nueva(request):
        if request.method == "POST":
            form = HabitacionForm(request.POST)
            if form.is_valid():
                precio = form.save()
                piso = form.save()
                maxpersonas = form.save()
                camabb = form.save()
                bano = form.save()
                balcon = form.save()
                fecha = form.save()
                
                messages.add_message(request, messages.SUCCESS, 'Reservacion Guardado Correctamente')
        else:
            form = HabitacionForm()
        return render(request, 'reservacion/habitacion_nuevo.html', {'form': form})

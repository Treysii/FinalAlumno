from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from .forms import AsignacionForm
from .forms import MateriaForm
from django.urls import reverse
from reservaciones.models import Materia,Grado,Asignacion
from django.contrib.auth.decorators import login_required



def lista(request):
    pub =Asignacion.objects.filter(fecha_publicacions__lte=timezone.now())
    return render(request, 'reservacion/listar.html', {'pub': pub})


def store(request):
    return render(request, 'reservacion/store.html')

def home(request):
    return render(request, 'reservacion/base.html')

def ver(request):
    return render(request, 'reservacion/ver.html')

@login_required
def materia_nueva(request):
    if request.method == "POST":
        form = HabitacionForm(request.POST)
        if form.is_valid():
            hab = form.save(commit=False)
            hab.save()
            return redirect('lista_habitacion')
    else:
        form = MateriaForm()
    return render(request, 'reservacion/habitacion_nuevo.html', {'form': form})

@login_required
def lista_materia(request):
    materia = Materia.objects.order_by('id')
    return render(request, 'reservacion/listahab.html', {'habitacion':habitacion})




@login_required
def materia_detalle(request, pk):
    materias = get_object_or_404(Materia, pk=pk)
    return render(request, 'reservacion/detallehab.html', {'habitaciones': habitaciones})

@login_required
def materia_editar(request, pk):
    habb = get_object_or_404(Materia, pk=pk)
    if request.method == "POST":
        form = MateriaForm(request.POST, instance=habb)
        if form.is_valid():
            habb = form.save(commit=False)
            habb.save()
            return redirect('lista_habitacion')
    else:
        form = MateriaForm(instance=habb)
    return render(request, 'reservacion/editarhab.html', {'form': form})

def materia_eliminar(request, pk):
    habit = get_object_or_404(Materia, pk=pk)
    habit.delete()
    return redirect('lista_habitacion')

@login_required
def asignacion_nueva(request):
    if request.method == "POST":
        formulario = AsignacionForm(request.POST)
        if formulario.is_valid():
            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'], seccion = formulario.cleaned_data['seccion'], fechaH = formulario.cleaned_data['fechaH'])
            for materia_id in request.POST.getlist('materias'):
                grados = Reserva(materia_id=materia_id, huesped_id = grado.id)
                grados.save()
            messages.add_message(request, messages.SUCCESS, 'Asignacion Guardado Correctamente')
    else:
        formulario = AsignacionForm()
    return render(request, 'reservacion/huesped_nuevo.html', {'formulario': formulario})

@login_required
def grado_editar(request, pk):
    grado = get_object_or_404(Grado, pk=pk)
    if request.method == "POST":
        form = AsignacionForm(request.POST, instance=grado)
        if form.is_valid():
            grado = form.save(commit=False)
            grado.save()
            return redirect('lista_huesped')
    else:
        form = AsignacionForm(instance=huesped)
    return render(request, 'reservacion/huesped_editar.html', {'form': form})

@login_required
def lista_grado(request):
    grados  = Grado.objects.order_by('fechaH')
    return render(request, 'reservacion/ver1.html', {'grados':grados})

@login_required
def huesped_detalle(request, pk):
    huespedes = get_object_or_404(Huesped, pk=pk)
    return render(request, 'reservacion/detallehues.html', {'huespedes': huespedes})

@login_required
def huesped_eliminar(request, pk):
    huesped = get_object_or_404(Huesped, pk=pk)
    huesped.delete()
    return redirect('lista_huesped')

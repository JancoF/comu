from .forms import ClienteForm
from django.http import  HttpResponse

from django.shortcuts import render, redirect

def formulario(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()

    return render(request, 'comunitarios/formulario.html', {'form': form})


# Create your views here.

def index(request):
    # Lógica de la vista
    return render(request,'comunitarios/index.html',{})



def programas(request):
    # Lógica de la vista
    return render(request,'Comunitarios/programas.html',{})


def servicios(request):
    # Lógica de la vista
    return render(request,'Comunitarios/servicios.html',{})



def contactos(request):
    # Lógica de la vista
    return render(request,'Comunitarios/contactos.html',{})


def suscripcion(request):
    # Lógica de la vista
    return render(request,'Comunitarios/suscripcion.html',{})


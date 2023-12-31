from django.shortcuts import render, redirect
from .models import Publicador

# Create your views here.
def home(request):
    publicadores = Publicador.objects.all()
    return render(request, 'index.html', {'publicadores':publicadores})

def adicionar(request):
    nome = request.POST.get('nome')
    batismo = request.POST.get('batismo')
    Publicador.objects.create(name=nome, baptism=batismo)
    publicadores = Publicador.objects.all()
    return render(request, 'index.html', {'publicadores':publicadores})

def editar(request, id):
    publicador = Publicador.objects.get(id=id)
    return render(request, 'update.html', {'publicador':publicador})

def update(request, id):
    publicador = Publicador.objects.get(id=id)
    new_name = request.POST.get('nome')
    new_baptism = request.POST.get('batismo')
    publicador.name = new_name
    publicador.baptism = new_baptism
    publicador.save()
    return redirect(home)

def deletar(request, id):
    publicador = Publicador.objects.get(id=id)
    publicador.delete()
    return redirect(home)
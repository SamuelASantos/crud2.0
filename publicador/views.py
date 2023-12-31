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
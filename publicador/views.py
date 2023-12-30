from django.shortcuts import render
from .models import Publicador

# Create your views here.
def home(request):
    publicadores = Publicador.objects.all()
    return render(request, 'index.html', {'publicadores':publicadores})
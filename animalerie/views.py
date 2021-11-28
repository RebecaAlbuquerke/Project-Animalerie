from django.shortcuts import render
from .models import Animal, Equipement

# Create your views here.
def index(request):
    animals = Animal.objects.order_by('nom_animal')
    equipements = Equipement.objects.order_by('nom_equipement')
    return render(request, 'index.html', {'animals': animals, 'equipements': equipements})

def animals(request):
    animals = Animal.objects.order_by('nom_animal')
    return render(request, 'animals.html', {'animals': animals})

def equipements(request):
    equipements = Equipement.objects.order_by('nom_equipement')
    return render(request, 'equipements.html', {'equipements': equipements})
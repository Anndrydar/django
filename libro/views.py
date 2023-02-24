from django.shortcuts import render
from .models import Projecto
from categoria.models import Catego

# Create your views here.

def vista_inicial(request):
    proyect=Projecto.objects.all()
    estanteria = Catego.objects.all().order_by('nombre')
    return render(request,'home.html',{'proyect':proyect, 'estanteria': estanteria})

def vista_filtro(request):
    nombre = request.GET['txttitulo']
    fil=Projecto.objects.filter(titulo__startswith=nombre)
    return render(request,'filtrolibro.html',{'fil':fil})

def vista_filtro2(request):
    libro = request.GET['txtname']
    fil=Projecto.objects.filter(titulo__startswith=libro)
    return render(request,'estanteria.html',{'fil':fil})

def vista_percha(request,nombre):
    estan = Projecto.objects.filter(grupo__nombre=nombre)
    return render(request,'estanteria.html', {'estan':estan})



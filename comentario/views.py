from django.shortcuts import render, redirect
from .models import Comentario
from libro.models import Projecto
from django.urls import reverse

# Create your views here.
def vista_comentarios(request):
    coment=Comentario.objects.all()
    return render(request,'comentario.html',{'coment':coment})

def vista_comentariolibro(request, titulo):
    proyect = Projecto.objects.filter(titulo=titulo)
    este = Comentario.objects.filter(libro__titulo = titulo)
    return render(request,'estecomentario.html',{'este':este,'proyect': proyect})

def hacerComentario(request):
    libro = request.POST['grupo']
    lector = request.POST['nombre']
    comentario = request.POST['descripcion']
    book = Projecto.objects.get(id=libro)
    publicacion = Comentario.objects.create(libro = book,lector=lector,descripcion=comentario)
    return redirect('/')



    

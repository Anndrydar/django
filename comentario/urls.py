from django.urls import path
from .views import vista_comentarios, vista_comentariolibro, hacerComentario

urlpatterns = [
    path('comentario/', vista_comentarios),
    path('comentariolibro/<titulo>', vista_comentariolibro),
    path('pos/', hacerComentario),
]

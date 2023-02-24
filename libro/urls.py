from django.urls import path
from .views import vista_inicial, vista_filtro, vista_filtro2, vista_percha


urlpatterns = [
    path('home/', vista_inicial),
    path('filtro/', vista_filtro),
    path('filtro2/', vista_filtro2),
    path('perchalibros/<nombre>', vista_percha),
]

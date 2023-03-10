from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from libro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.vista_inicial, name="home"),
    path('', include('comentario.urls')),
    path('', include('libro.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
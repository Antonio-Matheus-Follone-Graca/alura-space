from django.urls import path

from galeria.views import *
from galeria import views


urlpatterns = [
    path('', index, name='index'),
   path('imagem/<int:foto_id>', imagem, name='imagem'),
   path('buscar', buscar, name = "buscar")
    
]

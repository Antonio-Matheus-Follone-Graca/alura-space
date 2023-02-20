from django.urls import path

# importando views do app usuários
from usuarios.views import *



urlpatterns = [
   path('login',login, name='login'),
   path('cadastro',cadastro, name='cadastro'), 
]

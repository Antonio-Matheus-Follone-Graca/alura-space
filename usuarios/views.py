from django.shortcuts import render

# importando classe de formulario
from usuarios.forms import LoginForms
from usuarios.forms import CadastroForms
# Create your views here.

def login(request):
    form = LoginForms()
    # dicionario com formulario LoginForms
    contexto = {'form':form}
    return render(request, 'usuarios/login.html',contexto)
     

def cadastro(request):
    form_cadastro = CadastroForms()
    contexto = {'form': form_cadastro}
    return render(request, 'usuarios/cadastro.html',contexto) 





from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.

# importando model 
from galeria.models import Fotografia

from django.contrib import messages


def index( request):
    # se o usuário  não está logado
    if not request.user.is_authenticated:
        # redireciona para a página de login
        messages.error(request,' Usuário não logado')
        return redirect('login')
    else:
        # fazendo uma consulta dos dados da tabela
        fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada = True)

        return render(request,'galeria/index.html', {"cards": fotografias})


def imagem (request, foto_id):
    '''
        id_imagem: parametro id da imagem da url /imagem/<int:id_imagem>  
    '''
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    print(foto_id)
    # passando nome da imagem via dicionario
    print(fotografia)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        # redireciona para a página de login
        messages.error(request,' Usuário  não logado')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada = True)
    # se existe o campo de name buscar na requisição, faz a consulta 
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        print(nome_a_buscar)
        # se existe nome_a_buscar, se tem um valor nele
        if nome_a_buscar:
        # faz a consulta pelo campo nome da model
            fotografias = fotografias.filter(nome__icontains = nome_a_buscar)
   
            return render(request,'galeria/buscar.html',{"cards": fotografias})
    
    


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

# importando model 
from galeria.models import Fotografia


def index( request):
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
    return render(request,'pagina.html')



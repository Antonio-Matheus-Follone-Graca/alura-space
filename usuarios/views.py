from django.shortcuts import render,redirect

# importando classe de formulario
from usuarios.forms import LoginForms
from usuarios.forms import CadastroForms
from django.contrib.auth.models import  User
from django.contrib import auth
# Create your views here.

def login(request):
    form = LoginForms()
    if request.method == 'POST':
        # colocando dados do formulário na classe do formulário
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            # realizando login 
            usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
            )

            # se o login está correto
            if usuario is not None:
                # logando
                auth.login(request, usuario)
                # redirecionando para index
                return redirect('index')
            
            # caso a variavel usuário seja nulo 
            else:
                return redirect('login')

    
    # dicionario com formulario LoginForms
    contexto = {'form':form}
    return render(request, 'usuarios/login.html',contexto)
     

def cadastro(request):
    form_cadastro = CadastroForms()
    # se clicou no formulário 
    if request.method == 'POST':
        # colocando dados enviados do formulario no CadastroForms
        form = CadastroForms(request.POST)
        # validando formulário
        if form.is_valid():
            # se a senha 1 for diferente do senha 2
            if form['senha_1'].value() != form['senha_2'].value():
                return redirect('cadastro')
            

            # guardando valores dos campos no formulário
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha_1 = form['senha_1'].value()
            senha_2 = form['senha_2'].value()

            # validando o nome do usuário, se ele já existe
            if  User.objects.filter(username= nome).exists():
                return redirect('cadastro')

            else:

                # criando usuario 
                usuario = User.objects.create_user(
                    username= nome,
                    email= email,
                    password= senha_1
                )
                usuario.save()
                return redirect('login')
    
    contexto = {'form': form_cadastro}
    return render(request, 'usuarios/cadastro.html',contexto)


def logout(request):
    # deslogando usuário e redirecionando 
    auth.logout(request)
    return redirect('index')





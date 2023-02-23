from django.shortcuts import render, redirect

# importando formulários 
from usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

def login(request):
    form = LoginForms()

    # se clicou no formulário
    if request.method == 'POST':
        form = LoginForms(request.POST)
        # se o formulário for válido, faz a operação 
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
        # realizando o login
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        # se o login está correto
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
       # se clicou no formulário
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        # se o formulário for válido, faz a operação 
        if form.is_valid():
            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso!')
    return redirect('login')
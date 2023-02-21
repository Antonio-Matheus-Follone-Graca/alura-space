from django import forms

# formulario de cadastro
class CadastroForms(forms.Form):

    nome_cadastro = forms.CharField(
            label=' Nome Completo',
            required=  True, 
            max_length=100,
            widget= forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ex: João Silva'
                }
            )
            )

    email = forms.EmailField(label='Email', required= True, max_length= 100, widget= forms.EmailInput(
        attrs= { 
            'class': 'form-control',
            'placeholder':'joaosilva@xpto.com'
        } 
    ))   

    senha_1 = forms.CharField(label='Senha', required= True, max_length= 70, widget= forms.PasswordInput(
        attrs={
            "class": 'form-control',
            'placeholder':'Digite sua senha'
        } 
    )) 

    senha_2 = forms.CharField(label='Confirmação de senha', required= True, max_length= 70, widget= forms.PasswordInput(
        attrs={
            "class": 'form-control',
            'placeholder':' Digite sua senha mais uma vez'
        } 
    )) 
    

class LoginForms(forms.Form):
    # attrs sao os atributos do campo, coloquei um dicionario com a classe do campo e seu placeholder
    nome_login = forms.CharField(
        label=' Nome de login',
        required=  True, 
        max_length=100,
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Ex: João Silva'
            }
        )
        )
    # widget= forms.PasswordInput() deixa  o campo com type password
 
    senha = forms.CharField(label='Senha', required= True, max_length= 70, widget= forms.PasswordInput(
        attrs={
            "class": 'form-control',
            'placeholder':'Ex: Digite sua senha'
        } 
    ))
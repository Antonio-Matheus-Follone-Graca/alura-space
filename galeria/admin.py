from django.contrib import admin

from galeria.models import Fotografia

# configurações sobre o django admin 

# formatação da listagem de fotografias 
class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda')  # mostrando dados da tabela fotografia pelos campos id, nome e legenda
    list_display_links = ('id', 'nome') # mostrando links para o registro nos campos id e nome
    search_fields = ('nome',)  # pesquisar pelo campo nome, o virgula vazio é obrigatório  
 
 

# adicionando a opção da tabela fotografia, o segundo parametro e a classe de formatação de de fotografia
admin.site.register(Fotografia, ListandoFotografias)
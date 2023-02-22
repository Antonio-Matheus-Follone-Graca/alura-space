from django.contrib import admin

from galeria.models import Fotografia

# configurações sobre o django admin 

# formatação da listagem de fotografias 
class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', 'publicada')  # mostrando dados da tabela fotografia pelos campos id, nome, legenda e publicada
    list_display_links = ('id', 'nome') # mostrando links para o registro nos campos id e nome
    # a vírgula no final é obrigatória pois é uma tupla
    search_fields = ('nome',)  # pesquisar pelo campo nome, o virgula vazio é obrigatório  
    list_filter = ('categoria',"usuario") # filtro de registros por tipo de categoria e usuario
    list_per_page = 10 
    list_editable = ('publicada',) # campo que pode ser editado sem clicar no editar registro
 

# adicionando a opção da tabela fotografia, o segundo parametro e a classe de formatação de de fotografia
admin.site.register(Fotografia, ListandoFotografias)
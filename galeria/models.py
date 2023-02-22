from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Fotografia(models.Model):
    # lista com tuplas, pois o campo do tipo charfield só aceita formatos assim
    opcoes_categoria = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')    
    ]
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length = 100, choices= opcoes_categoria, default='')
    descricao = models.TextField(null=False, blank=False)
    # manda a imagem para a pasta fotos com foto com ano, mes e dia
    foto = models.ImageField(upload_to = 'fotos/%Y/%m/%d/', blank= True)
    publicada = models.BooleanField(default= False)
    data_fotografia = models.DateTimeField(default= datetime.now, blank = False)
    # chave estrangeira
    usuario = models.ForeignKey(
        to= User,
        on_delete=models.SET_NULL,
        null= True,
        blank= False,
        related_name= "user",
    )


    # ao chamar o objeto da classe retorna o nome da fotografia
    def __str__(self):
        return self.nome
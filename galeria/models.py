from django.db import models

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
    foto = models.CharField(max_length=150, null=False, blank=False)
    publicada = models.BooleanField(default= False)


    # ao chamar o objeto da classe retorna o nome da fotografia
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"
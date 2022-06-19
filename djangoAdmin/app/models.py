from django.db import models


class AnimalDomestico(models.Model):
    TIPO_CHOICES = (
        ("gato", "Gato"),
        ("cachorro", "Cachorro"),
    )
    SEXO_CHOICES = (
        ("feminino", "Feminino"),
        ("masculino", "Masculino"),
    )
    PORTE_CHOICES = (
        ("pequeno", "Pequeno"),
        ("médio", "Médio"),
        ("grande", "Grande"),
    )
    tipo = models.CharField(max_length=20, null=False, choices=TIPO_CHOICES)
    nome = models.CharField(max_length=50, null=False)
    entrada = models.DateField(null=False, verbose_name="Data de entrada do animal")
    sexo = models.CharField(max_length=20, null=False, choices=SEXO_CHOICES)
    prote = models.CharField(max_length=20, null=False, choices=PORTE_CHOICES)
    raca = models.CharField(max_length=20, null=False, verbose_name="Raça")
    vacinas = models.CharField(max_length=50)
    foto_animal = models.ImageField(upload_to='img')

    def __str__(self):
        return self.nome


class Campanha(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    data_evento = models.DateField(null=False, verbose_name="Data do Evento")
    local_evento = models.CharField(max_length=50, null=False, verbose_name="Local do Evento")
    texto = models.CharField(max_length=500, null=False)
    imagem_campanha = models.ImageField(upload_to='img')

    def __str__(self):
        return self.titulo

from django.db import models


# Create your models here.


class Topico(models.Model):
    nome = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.nome


class Webpage(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    nome = models.CharField(max_length=300, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.nome


class RegistroAcesso(models.Model):
    pagina = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    data = models.DateField()

    def __str__(self):
        return str(self.data)


class Pessoa(models.Model):
    referencia = models.ForeignKey(Topico, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True)
    email = models.EmailField()
    webpage = models.ForeignKey(Webpage, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

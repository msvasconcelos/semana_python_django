from django.db import models

# Create your models here.

class Tarefa(models.Model):
    PRIORIDADES_CHOICES = [
        ("A","Alta"),
        ("N", "Normal"),
        ("B", "Baixa")
    ]
    titulo = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    data_expiracao = models.DateField(null=False, blank=False)
    prioridade = models.CharField(max_length=1, choices=PRIORIDADES_CHOICES, null=False, blank=False)

class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=150,unique=True)
    profile = models.TextField()
    def __str__(self):
        return self.name
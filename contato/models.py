from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):  # pyright:ignore
        return self.nome


class Contato(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('Sobreno', max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    show = models.BooleanField(default=True)  # pyright:ignore
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, upload_to='images/%Y/%m')

    def __str__(self):   # pyright:ignore
        return self.nome

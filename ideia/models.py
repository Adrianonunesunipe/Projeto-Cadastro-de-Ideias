from django.db import models


VIABILIDADE_CHOICES = [
    ('1-Baixa', '1-Baixa'),
    ('2-Regular', '2-Regular'),
    ('3-Média', '3-Média'),
    ('4-Viável', '4-Viável'),
    ('5-Alta', '5-Alta')


]

SITUACAO_CHOICES = [
    ('Registrada', 'Registrada'),
    ('Em Desenvolvimento', 'Em Desenvolvimento'),
    ('Cancelada', 'Cancelada'),
    ('Desenvolvida', 'Desenvolvida')
]


class Ideia(models.Model):
    id = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=50)
    Sobrenome = models.CharField(max_length=50, blank=True, null=True)
    Nova_ideia = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nova Ideia')
    Descricao = models.CharField(max_length=250, blank=True, null=True, verbose_name='Descrição')
    Viabilidade = models.CharField(max_length=30, choices=VIABILIDADE_CHOICES, default=None)
    Situacao = models.CharField(max_length=30, choices=SITUACAO_CHOICES, default=None, verbose_name='Situação')
    Data = models.DateTimeField()

    def __str__(self):
        return self.pk

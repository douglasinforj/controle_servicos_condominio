from django.db import models
from django.contrib.auth.models import User, Group

#Controle de acesso:

from django.db.models.signals import post_migrate
from django.dispatch import receiver


class Condomino(models.Model):
    PROPRIETARIO = 'Proprietário'
    LOCADOR = 'Locador'
    TIPO_CHOICES = [
        (PROPRIETARIO, 'Proprietário'),
        (LOCADOR, 'Locador')
    ]


    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=25)
    email = models.EmailField()
    casa = models.CharField(max_length=10)
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=15, choices=TIPO_CHOICES)
    foto = models.ImageField(upload_to='condominios/', blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
class EmpresaParceira(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    responsavel_tecnico = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='empresas/', blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    documentos = models.FileField(upload_to='documentos/', blank=True, null=True)

    def __str__(self):
        return self.nome
    
class SolicitacaoServico(models.Model):
    ABERTO = 'Aberto'
    ANDAMENTO = 'Em Andamento'
    FINALIZADO = 'Finalizado'
    PENDENTE = 'Pendente'

    STATUS_CHOICES = [(ABERTO, 'Aberto'), (ANDAMENTO, 'Em Andamento'),
                      (FINALIZADO, 'Finalizado'), (PENDENTE, 'Pendente')]
    
    JARDINAGEM = 'Jardinagem'
    LIMPEZA = 'Limpeza'
    ELETRICA = 'Elétrica'
    
    TIPO_CHOICES = [(JARDINAGEM, 'Jardinagem'), (LIMPEZA, 'Limpeza'), (ELETRICA, 'Elétrica')]

    cabecalho = models.CharField(max_length=255)
    descricao = models.TextField()
    solicitante = models.ForeignKey(Condomino, on_delete=models.CASCADE)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    agendamento = models.DateTimeField(blank=True, null=True)
    tipo_servico = models.CharField(max_length=50, choices=TIPO_CHOICES)
    empresa_parceira = models.ForeignKey(EmpresaParceira, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ABERTO)

    def __str__(self):
        return f"{self.cabecalho} - {self.status}"
    
class Comentario(models.Model):
    solicitacao = models.ForeignKey(SolicitacaoServico, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    editado_por_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.username}: {self.comentario[:30]}"
    

#Criando Grupos para Controle de Acesso:
@receiver(post_migrate)
def criar_grupos(sender, **kwargs):
    if sender.name == 'servicos':
        Group.objects.get_or_create(name='Admin')
        Group.objects.get_or_create(name='Morador')
        Group.objects.get_or_create(name='EmpresaParceira')
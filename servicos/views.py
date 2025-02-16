from rest_framework import viewsets
from .models import Condomino, EmpresaParceira, SolicitacaoServico, Comentario
from .serializers import CondominoSerializer, EmpresaParceiraSerializer, SolicitacaoServicoSerializer, ComentarioSerializer

class CondôminoViewSet(viewsets.ModelViewSet):
    queryset = Condomino.objects.all()
    serializer_class = CondominoSerializer

class EmpresaParceiraViewSet(viewsets.ModelViewSet):
    queryset = EmpresaParceira.objects.all()
    serializer_class = EmpresaParceiraSerializer

class SolicitacaoServicoViewSet(viewsets.ModelViewSet):
    queryset = SolicitacaoServico.objects.all()
    serializer_class = SolicitacaoServicoSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
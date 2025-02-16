from rest_framework import serializers
from .models import Condomino, EmpresaParceira, SolicitacaoServico, Comentario


class CondominoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condomino
        fields = '__all__'

class EmpresaParceiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaParceira
        fields = '__all__'

class SolicitacaoServico(serializers.ModelSerializer):
    class Meta:
        model = SolicitacaoServico
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
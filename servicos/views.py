from rest_framework import viewsets
from .models import Condomino, EmpresaParceira, SolicitacaoServico, Comentario
from .serializers import CondominoSerializer, EmpresaParceiraSerializer, SolicitacaoServicoSerializer, ComentarioSerializer

#Controle e Permições
from rest_framework import permissions
from django.contrib.auth.models import Group



#Permissões Personalizadas para diferenciar acesso:
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_superuser or request.user.groups.filter(name='admin').exists()
        )

class IsMoradorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.groups.filter(name='Morador').exists() or request.user.groups.filter(name='Admin').exists()
        )

class IsEmpresaOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.groups.filter(name='EmpresaParceira').exists() or request.user.groups.filter(name='Admin').exists()
        )


#---------------------Views----API-------------------------

class CondominoViewSet(viewsets.ModelViewSet):
    queryset = Condomino.objects.all()
    serializer_class = CondominoSerializer
    permission_classes= [IsAdminOrReadOnly]     #aplicando as permissões

class EmpresaParceiraViewSet(viewsets.ModelViewSet):
    queryset = EmpresaParceira.objects.all()
    serializer_class = EmpresaParceiraSerializer
    permission_classes =[IsAdminOrReadOnly]     #aplicando permissões

class SolicitacaoServicoViewSet(viewsets.ModelViewSet):
    queryset = SolicitacaoServico.objects.all()
    serializer_class = SolicitacaoServicoSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [permissions.IsAuthenticated()]
        elif self.request.method in ['POST']:
            return [IsMoradorOrAdmin()]
        else:
            return [IsEmpresaOrAdmin()]


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsMoradorOrAdmin()]
        elif self.request.method in ['DELETE']:
            return [IsAdminOrReadOnly()]
        return [permissions.IsAuthenticated()]
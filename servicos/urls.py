from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CondominoViewSet, EmpresaParceiraViewSet, SolicitacaoServicoSerializer, ComentarioViewSet

router = DefaultRouter()
router.register(r'condominos', CondominoViewSet)
router.register(r'empresas', EmpresaParceiraViewSet)
router.register(r'solicitacoes', SolicitacaoServicoSerializer)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls)), 
]
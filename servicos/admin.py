from django.contrib import admin
from .models import Condomino, EmpresaParceira, SolicitacaoServico, Comentario

@admin.register(Condomino)
class CondominoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'email', 'casa', 'numero', 'tipo')  
    search_fields = ('nome', 'cpf', 'email')  
    list_filter = ('tipo',)  
    ordering = ('nome',)  

@admin.register(EmpresaParceira)
class EmpresaParceiraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone', 'responsavel_tecnico')  
    search_fields = ('nome', 'cnpj', 'responsavel_tecnico')  
    list_filter = ('responsavel_tecnico',)  
    ordering = ('nome',)  

@admin.register(SolicitacaoServico)
class SolicitacaoServicoAdmin(admin.ModelAdmin):
    list_display = ('cabecalho', 'solicitante', 'data_solicitacao', 'agendamento', 'tipo_servico', 'empresa_parceira', 'status')  
    search_fields = ('cabecalho', 'solicitante__nome', 'empresa_parceira__nome')  
    list_filter = ('status', 'tipo_servico', 'empresa_parceira')  
    ordering = ('-data_solicitacao',)  

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('solicitacao', 'usuario', 'data', 'comentario_resumido', 'editado_por_admin')  
    search_fields = ('solicitacao__cabecalho', 'usuario__username', 'comentario')  
    list_filter = ('data', 'editado_por_admin')  
    ordering = ('-data',)  

    def comentario_resumido(self, obj):
        return obj.comentario[:50] + "..." if len(obj.comentario) > 50 else obj.comentario
    comentario_resumido.short_description = "Comentário"

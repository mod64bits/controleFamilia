from django.urls import path, re_path
from .views import DeletarCategoria, AtualizarCategoria, NovaCategoria, DealhesCategoria, ListaCategoria
from .views import NovaDespesa, DespesaDetalhe, ListarDespesas, AtualizarDespesa, ApagarDespesa



urlpatterns = [
    path('deletar-categoria/<slug:slug>', DeletarCategoria.as_view(),
         name='deletar_categoria'),
    path('atualizar-forma-de-pagamento/<slug:slug>', AtualizarCategoria.as_view(),
         name='atualizar_categoria'),
    path('nova-forma-de-pagamento/', NovaCategoria.as_view(), name='nova_categoria'),
    path('detalhes-categoria/<slug:slug>', DealhesCategoria.as_view(),
         name='detalhe_categoria'),
    path('listar-categoria/', ListaCategoria.as_view(), name='listar_categoria'),
    #Despesas URLS
    path('nova-despesa/', NovaDespesa.as_view(), name='nova_despesa'),
    path('detalhes-despesa/<slug:slug>', DespesaDetalhe.as_view(), name='detalhe_despesa'),
    path('listar-despesa/', ListarDespesas.as_view(), name='listar_despesa'),
    path('atualizar-despesa/<slug:slug>', AtualizarDespesa.as_view(), name='atualizar_despesa'),
    path('deletar-despesa/<slug:slug>', ApagarDespesa.as_view(), name='deletar_despesa'),
]

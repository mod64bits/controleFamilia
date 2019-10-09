from django.urls import path, re_path
from .views import (NovaFormaDePagamento, ListarFormaDePagamento, DetalheFormaDePagamento, AtualizarFormaDePagamento,
                    DeletarFormaDePagamento)
from .views import (NovaReceita, ListarReceita, DetalheReceita, AtualizarReceita, DeletarReceita)


urlpatterns = [
    path('deletar-forma-de-pagamento/<slug:slug>', DeletarFormaDePagamento.as_view(),
         name='deletar_forma_de_pagamento'),
    path('atualizar-forma-de-pagamento/<slug:slug>', AtualizarFormaDePagamento.as_view(),
         name='atualizar_forma_de_pagamento'),
    path('nova-forma-de-pagamento/', NovaFormaDePagamento.as_view(), name='nova_forma_de_pagamento'),
    path('detalhes-forma-de-pagamento/<slug:slug>', DetalheFormaDePagamento.as_view(),
         name='detalhe_forma_de_pagamento'),
    path('listar-forma-de-pagamento/', ListarFormaDePagamento.as_view(), name='listar_forma_de_pagamento'),

   #Receitas URLs
    path('deletar-receita/<slug:slug>', DeletarReceita.as_view(),
         name='deletar_receita'),
    path('atualizar-receita/<slug:slug>', AtualizarReceita.as_view(),
         name='atualizar_receita'),
    path('nova-receita/', NovaReceita.as_view(), name='nova_receita'),
    path('detalhes-receita/<slug:slug>', DetalheReceita.as_view(),
         name='detalhe_receita'),
    path('listar-receita/', ListarReceita.as_view(), name='listar_receita'),

]

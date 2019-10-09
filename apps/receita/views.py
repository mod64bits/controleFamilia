from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import FormaDePagamento, Receita


class NovaFormaDePagamento(LoginRequiredMixin, CreateView):
    model = FormaDePagamento
    fields = '__all__'

class DetalheFormaDePagamento(LoginRequiredMixin, DetailView):
    model = FormaDePagamento
    template_name = 'receita/detalheFormaPagamento.html'

class ListarFormaDePagamento(ListView):
    model = FormaDePagamento
    template_name = 'receita/ListarFormaPagamento.html'
    paginate_by = 25

class AtualizarFormaDePagamento(LoginRequiredMixin, UpdateView):
    model = FormaDePagamento
    fields = '__all__'
    template_name = 'receita/formadepagamento_form.html'


class DeletarFormaDePagamento(LoginRequiredMixin, DeleteView):
    model = FormaDePagamento
    success_url = reverse_lazy('listar_forma_de_pagamento')

'''
Receita
'''
class NovaReceita(LoginRequiredMixin, CreateView):
    model = Receita
    fields = '__all__'


class DetalheReceita(LoginRequiredMixin, DetailView):
    model = Receita
    template_name = 'receita/detalheReceita.html'


class ListarReceita(LoginRequiredMixin, ListView):
    model = Receita
    template_name = 'receita/ListarReceita.html'
    paginate_by = 25

class AtualizarReceita(LoginRequiredMixin, UpdateView):
    model = Receita
    fields = '__all__'
    template_name = 'receita/receita_form.html'

class DeletarReceita(LoginRequiredMixin, DeleteView):
    model = Receita
    template_name = 'receita/receita_confirm_delete.html'
    success_url = reverse_lazy('listar_receita')






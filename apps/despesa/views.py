from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import DespesaCreateForm
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import CategoriaDespesa, Despesa


class NovaCategoria(LoginRequiredMixin, CreateView):
    model = CategoriaDespesa
    fields = '__all__'
    template_name = 'despesa/categoria_form.html'

class DealhesCategoria(LoginRequiredMixin, DetailView):
    model = CategoriaDespesa
    template_name = 'despesa/detalheCategoria.html'


class ListaCategoria(LoginRequiredMixin, ListView):
    model = CategoriaDespesa
    template_name = 'despesa/ListarCategoria.html'
    paginate_by = 25


class AtualizarCategoria(LoginRequiredMixin, UpdateView):
    model = CategoriaDespesa
    fields = '__all__'
    template_name = 'despesa/categoria_form.html'


class DeletarCategoria(LoginRequiredMixin, DeleteView):
    model = CategoriaDespesa
    success_url = reverse_lazy('listar_categoria')


class NovaDespesa(LoginRequiredMixin, CreateView):
    model = Despesa
    form_class = DespesaCreateForm
    template_name = 'despesa/despesa_form.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

        # chave usuario em kwargs


    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(NovaDespesa, self).get_form_kwargs(*args, **kwargs)
        kwargs['usuario'] = self.request.user
        return kwargs


class DespesaDetalhe(LoginRequiredMixin, DetailView):
    model = Despesa
    template_name = 'despesa/detalheDespesa.html'

class ListarDespesas(ListView):
    model = Despesa
    template_name = 'despesa/ListarDespesa.html'


class AtualizarDespesa(LoginRequiredMixin, UpdateView):
    model = Despesa
    fields = '__all__'
    template_name = 'despesa/despesa_form.html'


class ApagarDespesa(LoginRequiredMixin, DeleteView):
    model = Despesa
    success_url = reverse_lazy('listar_despesa')


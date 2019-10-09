from django.db import models
from django.db.models import signals
from apps.core.signals import create_slug
from django.urls import reverse


class FormaDePagamento(models.Model):
    nome = models.CharField('Forma de Pagamento', max_length=100, help_text='Dinheiro Cartão Etc')
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'
    descricao = models.TextField('Descrição', help_text='Uma Breve Descrição ', blank=True, null=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def get_absolute_url(self):
        return reverse('detalhe_forma_de_pagamento', kwargs={'slug': self.slug})

    def __str__(self):
        return self.nome


signals.post_save.connect(create_slug, sender=FormaDePagamento)


class Receita(models.Model):
    receita_nome = models.CharField('Nome da Receita', max_length=100, help_text='Nome da Receita')
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'receita_nome'
    descricao = models.TextField('Descrição', help_text='Uma Breve Descrição da Receita', blank=True, null=True)
    valor = models.DecimalField('Valor', help_text='Valor Total da Receita', decimal_places=2, max_digits=8)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def get_absolute_url(self):
        return reverse('detalhe_receita', kwargs={'slug': self.slug})

    def __str__(self):
        return self.receita_nome


signals.post_save.connect(create_slug, sender=Receita)



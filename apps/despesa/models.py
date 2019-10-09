from django.contrib.auth.models import User
from django.db import models
from django.db.models import signals
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.core.signals import create_slug
from apps.relatorios.manager import RelatoriosManager



class CategoriaDespesa(models.Model):
    nome = models.CharField('Nome', max_length=60, help_text='Nome da Categoria')
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'
    descricao = models.TextField('Descrição', help_text='Uma Breve Descrição da Categoria', blank=True, null=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def get_absolute_url(self):
        return reverse('detalhe_categoria', kwargs={'slug': self.slug})

    def __str__(self):
        return self.nome


signals.post_save.connect(create_slug, sender=CategoriaDespesa)


class Despesa(models.Model):
    nome = models.CharField('Nome', max_length=60, help_text='Titulo da Dispesa')
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    slug_from = 'nome'
    categoria = models.ForeignKey(CategoriaDespesa, verbose_name='Categoria da Despesa', on_delete=models.SET_NULL,
                                  null=True, blank=True)
    data = models.DateField('Data do Pagamento ex: 20/05/2019', help_text='Data Do Pagamento', blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, editable=False)
    descricao = models.TextField('Descrição', help_text='Descrição', blank=True, null=True)
    valor = models.DecimalField('Valor', decimal_places=2, max_digits=8)
    STATE_CHOICES = (
        ('Nao', u'Não Pago'),
        ('Pago', u'PAGO'),
    )
    estado = models.CharField(max_length=10, choices=STATE_CHOICES, default='Pago', verbose_name='Estado')
    doc = models.ImageField('Imagens', upload_to='docs/%Y-%m-%d', blank=True, null=True)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    objects = RelatoriosManager()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.User
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(Despesa, self).get_form_kwargs(*args, **kwargs)
        kwargs['usuario'] = self.request.User
        return kwargs

    def get_absolute_url(self):
        return reverse('detalhe_despesa', kwargs={'slug': self.slug})

    def __str__(self):
        return self.nome


signals.post_save.connect(create_slug, sender=Despesa)


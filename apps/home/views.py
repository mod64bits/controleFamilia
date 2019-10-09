from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Avg, Count, Min, Sum
from apps.despesa.models import Despesa
from datetime import date


class Home(ListView):
    model = Despesa
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        gastosAnuais = Despesa.objects.all().aggregate(Sum('valor'))['valor__sum']
        mes = str(date.today().month)
        mes_anterior = str(date.today().month -1)
        dia = str(date.today().day)

        depesas_mensais = Despesa.objects.filter(data__month=mes).aggregate(Sum('valor'))['valor__sum']
        depesas_mes_anterior = Despesa.objects.filter(data__month=mes_anterior).aggregate(Sum('valor'))['valor__sum']
        depesas_diarias = Despesa.objects.filter(data__day=dia).aggregate(Sum('valor'))['valor__sum']

        context = super().get_context_data(**kwargs)
        context['gastosAnuais'] = gastosAnuais
        context['depesas_mensais'] = depesas_mensais
        context['depesas_mes_anterior'] = depesas_mes_anterior
        context['depesas_diarias'] = depesas_diarias

        return context

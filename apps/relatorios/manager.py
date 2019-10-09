from django.db import models
from datetime import date
from django.db.models import Avg, Count, Min, Sum


class RelatoriosManager(models.Manager):
    def gasto_anual(self):
        return self.all().aggregate(Sum('valor'))['valor__sum']

    def gastos_mensais(self):
        mes = str(date.today().month)
        return self.filter(data__month=mes).aggregate(Sum('valor'))['valor__sum']

    def gastos_mes_anterior(self):
        mes = str(date.today().month - 1)
        return self.filter(data__month=mes).aggregate(Sum('valor'))['valor__sum']


    def gastos_diarios(self):
        dia = str(date.today().day)
        return self.filter(data__day=dia).aggregate(Sum('valor'))['valor__sum']


    def gastos_usuarios(self):
        return self.filter(usuario__despesa=id(id)).aggregate(Sum('valor'))['valor__sum']


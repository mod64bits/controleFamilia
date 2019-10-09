from django.shortcuts import render
from apps.despesa.models import Despesa
from django.views import View


class Relatorios(View):
    def get(self, request):
        data={}
        data['gasto_anual'] = Despesa.objects.gasto_anual()
        data['gastos_mensais'] = Despesa.objects.gastos_mensais()
        data['mes_anterior'] = Despesa.objects.gastos_mes_anterior()
        data['gastos_diarios'] = Despesa.objects.gastos_diarios()
        data['gastos_usuarios'] = Despesa.objects.gastos_usuarios()

        return render(request, 'relatorios/home.html', data)




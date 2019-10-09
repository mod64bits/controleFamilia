from django.urls import path, re_path
from .views import Relatorios


urlpatterns = [
    path('', Relatorios.as_view(), name='relatorios'),

]

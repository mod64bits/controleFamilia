from django.urls import path, re_path, include
from .views import registrar


urlpatterns = [
    path('', registrar, name='novo_usurio'),
]

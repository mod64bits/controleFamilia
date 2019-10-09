"""ControleFamilia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.receita import urls as receita_url
from apps.despesa import urls as despesa_url
from apps.usuarios import urls as usuarios_url
from apps.home import urls as home_urls
from apps.relatorios import urls as relatorios_urls

urlpatterns = [
    path('', include(home_urls)),
    path('relatorios/', include(relatorios_urls)),
    path('despesa/', include(despesa_url)),
    path('receita/', include(receita_url)),
    path('admin/', admin.site.urls),
    path('usuarios/', include(usuarios_url)),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

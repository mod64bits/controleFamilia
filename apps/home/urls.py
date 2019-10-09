from django.urls import path, re_path
from .views import Home


urlpatterns = [
    path('', Home.as_view(), name='home'),

]

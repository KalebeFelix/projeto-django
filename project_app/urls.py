# INDICANDOS AS ROTAS

from django.urls import path
from . import views

urlpatterns = [

    # INDO PARA A VIEW 
    path('', views.index),
]

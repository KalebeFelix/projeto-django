# INDICANDOS AS ROTAS

from django.urls import path
from . import views

urlpatterns = [

    # INDO PARA A VIEW 
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path('topic/<topic_id>/', views.topic, name='topic'),
]

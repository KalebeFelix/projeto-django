from django.shortcuts import render
from .models import Topic

def index(request):
    # PAGINA HTML INICIAL, vai tratar a requisição
    return render(request, 'project_app/index.html')

def topics(request):
    # PAGINA DE ASSUNTOS 
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    # PASSANDO DADOS DO DATABASE PARA A TELA
    return render(request, 'project_app/topics.html', context)

def topic(request, topic_id):
    # PAGINA DE ASSUNTOS 
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'project_app/topic.html', context)
    

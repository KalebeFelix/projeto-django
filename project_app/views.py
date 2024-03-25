from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .form import TopicForm, EntryForm
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
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'project_app/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        # NÃO ENVIADO
        form = TopicForm()
    else:
        # ENVIADO
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request, 'project_app/new_topic.html', context)

def new_entry(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    if request.method != 'POST':
        # NÃO ENVIADO
        form = EntryForm()
    else:
        # ENVIADO
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'project_app/new_entry.html', context)
    

from django.shortcuts import render

def index(request):
    # PAGINA HTML INICIAL, vai tratar a requisição
    return render(request, 'project_app/index.html')

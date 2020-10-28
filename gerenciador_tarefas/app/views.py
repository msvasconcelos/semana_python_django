from django.shortcuts import render

# Create your views here.

def listar_tarefas(request):
    nome_tarefa = "Assistir a semana Python Django"
    return render(request, 'tarefas/listar_tarefas.html', {"nome_tarefa": nome_tarefa})
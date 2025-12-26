# tarefas/views.py
from django.shortcuts import render
from datetime import date
from .models import Tarefa

def lista_tarefas(request):
    # Buscar todas as tarefas ordenadas por prazo
    tarefas = Tarefa.objects.all().order_by('prazo', 'status')
    
    # Data atual para verificar atrasos
    hoje = date.today()
    
    # Contexto para o template
    context = {
        'tarefas': tarefas,
        'hoje': hoje,
        'total_tarefas': tarefas.count(),
        'tarefas_pendentes': tarefas.filter(status='pendente').count(),
        'tarefas_concluidas': tarefas.filter(status='concluida').count(),
        'tarefas_atrasadas': tarefas.filter(prazo__lt=hoje).exclude(status='concluida').count(),
    }
    
    return render(request, 'lista_tarefas.html', context)
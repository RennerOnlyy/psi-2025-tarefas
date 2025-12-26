from django.db import models

class Tarefa(models.Model):
    # Opções para status
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
    ]
    
    nome = models.CharField(
        max_length=200,
        verbose_name='Nome da Tarefa'
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente',
        verbose_name='Status'
    )
    
    prazo = models.DateField(
        verbose_name='Prazo de Conclusão'
    )
    
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )
    
    def __str__(self):
        return f"{self.nome} - {self.get_status_display()}"
    
    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['prazo', 'status']
# tarefas/admin.py
from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'status', 'prazo', 'data_criacao', 'esta_atrasada')
    list_filter = ('status', 'prazo')
    search_fields = ('nome',)
    date_hierarchy = 'prazo'
    
    fieldsets = (
        ('Informações da Tarefa', {
            'fields': ('nome', 'status')
        }),
        ('Datas', {
            'fields': ('prazo', 'data_criacao')
        }),
    )
    
    readonly_fields = ('data_criacao',)
    
    def esta_atrasada(self, obj):
        from datetime import date
        return obj.prazo < date.today() and obj.status != 'concluida'
    
    esta_atrasada.boolean = True
    esta_atrasada.short_description = 'Atrasada?'
    esta_atrasada.admin_order_field = 'prazo'
# blog/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_publicacao', 'publicado', 'imagem_preview')
    list_filter = ('publicado', 'data_publicacao')
    search_fields = ('titulo', 'conteudo')
    date_hierarchy = 'data_publicacao'
    
    fieldsets = (
        ('Informações do Post', {
            'fields': ('titulo', 'conteudo', 'publicado')
        }),
        ('Imagem', {
            'fields': ('imagem', 'imagem_preview')
        }),
        ('Datas', {
            'fields': ('data_publicacao', 'data_criacao'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('data_criacao', 'imagem_preview')
    
    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html(
                '<img src="{}" width="150" style="border-radius: 5px;" />',
                obj.imagem.url
            )
        return "Sem imagem"
    
    imagem_preview.short_description = 'Pré-visualização'
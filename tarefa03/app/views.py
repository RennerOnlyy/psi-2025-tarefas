from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def usuarios(request):
    # Lista de 5 usuários fictícios
    lista_usuarios = [
        {
            'nome': 'Ana Silva',
            'matricula': '2024001',
            'idade': 25,
            'cidade': 'São Paulo'
        },
        {
            'nome': 'Bruno Oliveira',
            'matricula': '2024002', 
            'idade': 32,
            'cidade': 'Rio de Janeiro'
        },
        {
            'nome': 'Carla Santos',
            'matricula': '2024003',
            'idade': 28,
            'cidade': 'Belo Horizonte'
        },
        {
            'nome': 'Daniel Costa',
            'matricula': '2024004',
            'idade': 22,
            'cidade': 'Porto Alegre'
        },
        {
            'nome': 'Eduarda Lima',
            'matricula': '2024005',
            'idade': 30,
            'cidade': 'Salvador'
        }
    ]
    
    context = {
        'usuarios': lista_usuarios,
        'total_usuarios': len(lista_usuarios)
    }
    
    return render(request, 'usuarios.html', context)
from django.shortcuts import render

from .models import Produto


def index(request):
    if str(request.user) == 'AnonymousUser':
        logado = 'Usuário não logado'
    else:
        logado = f'Usuário logado: {str(request.user)}'

    produtos = Produto.objects.all()

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!',
        'logado': logado,
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    context = {
        'produto': Produto.objects.get(id=pk)
    }
    return render(request, 'produto.html', context)

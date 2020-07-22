from django.shortcuts import render


def index(request):
    if str(request.user) == 'AnonymousUser':
        logado = 'Usuário não logado'
    else:
        logado = f'Usuário logado: {str(request.user)}'

    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!',
        'logado': logado
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')

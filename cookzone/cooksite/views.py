from django.shortcuts import render

from django.shortcuts import render


def index(request):
    context = {
        'products': ['Товар 1', 'Товар 2', 'Товар 3'],
    }
    return render(request, 'cooksite/index.html', context)

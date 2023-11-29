from django.shortcuts import render
from django.http import HttpResponse

from clientes.models import Clientes


def get(request):
    queryset = Clientes.objects.all()
    context = {'lista_clientes': queryset}
    return render(request, 'clientes/clientes.html', context)
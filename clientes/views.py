from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from clientes.models import Clientes
from django.http import HttpResponseRedirect
from django.urls import reverse


def get(request):
    queryset = Clientes.objects.all()
    context = {'lista_clientes': queryset}
    return render(request, 'clientes/clientes.html', context)


def retrieve(request, cliente_id):
    cliente = get_object_or_404(Clientes, pk=cliente_id)
    return render(request, 'clientes/cliente-detalle.html', {'instancia': cliente})


def update(request, cliente_id):
    cliente = get_object_or_404(Clientes, pk=cliente_id)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.nit = request.POST['nit']
        cliente.nombre_contacto = request.POST['nombre_contacto']
        cliente.telefono = request.POST['tel']
        cliente.direccion = request.POST['direccion']
        cliente.correo = request.POST['correo']

        cliente.save()

    return render(request, 'clientes/cliente-actualizar.html', {'instancia': cliente})


def post(request):
    print(request.method)
    print(request.POST)
    if request.method == 'POST':
        Clientes.objects.create(
            nombre=request.POST['nombre'],
            nit=request.POST['nit'],
            nombre_contacto=request.POST['nombre_contacto'],
            telefono=request.POST['tel'],
            direccion=request.POST['direccion'],
            correo=request.POST['correo']
        )
        
    return render(request, 'clientes/cliente-crear.html') 


def delete(request, cliente_id):
    cliente = get_object_or_404(Clientes, pk=cliente_id)
    cliente.delete()
    return HttpResponseRedirect(reverse('clientes:get'))

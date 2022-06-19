from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import AnimalDomestico, Campanha


def index(request, template_name="index.html"):
    return render(request, template_name)

def sobre(request, template_name="sobre.html"):
    return render(request, template_name)

def apoie(request, template_name="apoie.html"):
    return render(request, template_name)

def listar_animais(request, template_name="adocao.html"):
    page = request.GET.get('page', '')
    ordenar = request.GET.get("ordenar", '')

    try:
        if ordenar:
            animal = AnimalDomestico.objects.all().order_by(ordenar)
        else:
            animal = AnimalDomestico.objects.all()
        animal = Paginator(animal, 3)
        animal = animal.page(page)
    except PageNotAnInteger:
        animal = animal.page(1)

    except EmptyPage:
        animal = paginator.page(paginator.num_paginas)
    animais = {'lista': animal}
    return render(request, template_name, animais)


def listar_campanhas(request, template_name="campanhas.html"):
    query = request.GET.get("busca", '')
    page = request.GET.get('page', '')
    ordenar = request.GET.get("ordenar", '')
    if query:
        campanha = Campanha.objects.filter(titulo__icontains=query)
    else:
        try:
            if ordenar:
                campanha = Campanha.objects.all().order_by(ordenar)
            else:
                campanha = Campanha.objects.all()
            campanha = Paginator(campanha, 2)
            campanha = campanha.page(page)

        except PageNotAnInteger:
            campanha = campanha.page(1)

        except EmptyPage:
            campanha = paginator.page(paginator.num_paginas)

    campanhas = {'lista': campanha}
    return render(request, template_name, campanhas)


def perfil_animal(request, pk, template_name="perfil_animal.html"):
    animal = get_object_or_404(AnimalDomestico, pk=pk)
    return render(request, template_name, {'animal': animal})


def campanha_view(request, pk, template_name="campanha_view.html"):
    campanha = get_object_or_404(Campanha, pk=pk)
    return render(request, template_name, {'campanha': campanha})


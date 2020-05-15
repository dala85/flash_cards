from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from .models import Choicess
from . import models
import random
from django.urls import reverse, reverse_lazy

# Create your views here.
id_list = []
counter = 0


def choicess_aq(request):
    global counter
    if request.method == 'POST':
        choice_selected = Choicess.objects.get(pk=id_list[counter])
        if counter >= (len(id_list) - 1):
            counter = 0
        else:
            counter += 1

        if request.POST.get('correct'):
            print(request.POST)

    template_name = 'choicess/test.html'
    context = {'choice': choice_selected}
    return render(request, template_name, context)


def choicess_view(request):
    choice_set = Choicess.objects.all()
    for choice in choice_set.iterator():
        global id_list
        id_list.append(choice.id)
    obj = Choicess.objects.all()
    template_name = 'choicess/test.html'
    context = {'choice': choice}
    return render(request, template_name, context)
#

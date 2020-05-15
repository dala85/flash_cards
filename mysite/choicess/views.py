from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from .models import Choicess
from . import models
import random
from django.urls import reverse, reverse_lazy

id_list = []
counter = 0
user_answer = []
stop = 1


def choicess_qa(request):
    global stop
    global counter
    global user_answer
    if counter >= (len(id_list) - 1):
        stop = 0
    if request.method == 'POST':
        choice_selected = Choicess.objects.get(pk=id_list[counter])
        if counter >= (len(id_list) - 1):
            counter = 0
        else:
            counter += 1
        if request.POST.get('correct'):
            user_answer.append(1)
        else:
            user_answer.append(2)

    print(user_answer, counter, len(id_list))
    template_name = 'choicess/choicess_view.html'

    context = {'choice': choice_selected,
               'user_answer': user_answer, 'stop': stop}

    return render(request, template_name, context)


def choicess_view(request):
    global id_list
    global user_answer
    global stop
    stop = 1
    id_list = []
    user_answer = []
    choice_set = Choicess.objects.all()
    for choice in choice_set.iterator():
        id_list.append(choice.id)
    obj = Choicess.objects.all()
    template_name = 'choicess/choicess_view.html'
    context = {'choice': choice}
    return render(request, template_name, context)


def result_view(request):
    obj = Choicess.objects.all()
    template_name = 'choicess/test.html'
    print(user_answer)

    context = {'choice': obj, 'colored_card': user_answer}
    return render(request, template_name, context)

    #

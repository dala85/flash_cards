from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from .models import Cards
from . import models
import random
from django.urls import reverse, reverse_lazy


# Create your views here.


def home_view(request):

    obj = Cards.objects.all()
    template_name = 'cards/flash_cards.html'
    random_number = random.randint(1, 3)

    context = {'obj': obj, 'random_number': random_number}
    return render(request, template_name, context)


def cards_list(request):
    template_name = 'cards/test2.html'
    if request.method == 'POST':
        Cards.objects.create(title=request.POST.get('title'),
                             question=request.POST.get('question'),
                             answer=request.POST.get('answer'))

    obj = Cards.objects.all()
    context = {'obj': obj}

    return render(request, template_name, context)


class CardsDeleteView(DeleteView):

    model = models.Cards
    success_url = reverse_lazy('cards_list')
    #

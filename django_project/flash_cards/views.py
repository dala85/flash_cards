from django.shortcuts import render
from .models import Cards
from .forms import CardsForm
import random


# Create your views here.


def home_view(request):

    obj = Cards.objects.all()
    template_name = 'flash_cards/flash_cards.html'
    random_number = random.randint(1, 3)

    context = {'obj': obj, 'random_number': random_number}
    return render(request, template_name, context)


def fill_cards(request):
    if request.method == 'POST':
        # title = request.POST.get('title')
        # question = request.POST.get('question')
        # answer = request.POST.get('answer')
        form = CardsForm(request.POST)
        if form.is_valid():

            obj = Cards.objects.create(
                title=form.cleaned_data.get('title'),
                question=form.cleaned_data.get('question'),
                answer=form.cleaned_data.get('answer'),
                choice_a=form.cleaned_data.get('choice_a'),
                choice_b=form.cleaned_data.get('choice_b'),
                choice_c=form.cleaned_data.get('choice_c'),
                choice_d=form.cleaned_data.get('choice_d'),
            )

    context = {}

    return render(request, 'flash_cards/fill_cards.html', context)

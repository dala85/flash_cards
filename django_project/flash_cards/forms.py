from django import forms
from .models import Cards, Section


class SectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = '__all__'


class CardsForm(forms.ModelForm):

    class Meta:
        model = Cards
        fields = '__all__'

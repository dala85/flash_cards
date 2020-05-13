from django.db import models


class Section(models.Model):
    section = models.CharField(max_length=150)


class Cards(models.Model):
    title = models.ForeignKey(Section, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    choice_a = models.CharField(max_length=200)
    choice_b = models.CharField(max_length=200)

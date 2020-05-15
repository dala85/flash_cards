from django.db import models

# Create your models here.


class Choicess(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    choice_a = models.CharField(max_length=200, null=True, blank=True)
    choice_b = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.question

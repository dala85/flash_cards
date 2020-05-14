from django.db import models


class Cards(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    question = models.CharField(max_length=200, null=True, blank=True)
    answer = models.CharField(max_length=200, null=True, blank=True)
    choice_a = models.CharField(max_length=200, null=True, blank=True)
    choice_b = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cards:view_settings', kwargs={'pk': self.pk})

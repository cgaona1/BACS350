from django.db import models
from django.urls.base import reverse_lazy

# Create your models here.
class Hero(models.Model):
    hero_name = models.CharField(max_length=50)
    hero_description = models.CharField(max_length=200)
    hero_image = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.hero_name}'

    def get_absolute_url(self):
        return reverse_lazy('hero_detail', args=[str(self.id)])

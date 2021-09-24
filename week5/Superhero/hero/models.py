from django.db import models

# Create your models here.


class Hero(models.Model):
    hero_name = models.CharField(max_length=50)
    hero_description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.hero_name}'

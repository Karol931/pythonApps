from django.db import models

# Create your models here.

class Game(models.Model):
    lifes = models.IntegerField()
    original_word = models.CharField(max_length=20)
    guessed_word = models.CharField(max_length=20, default="")


class Letters(models.Model):
    letters = models.CharField(max_length=1, unique=True)


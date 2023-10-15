from django.db import models

# Create your models here.

class Game(models.Model):
    lifes = models.IntegerField()
    original_word = models.CharField(max_length=20)
    guessed_word = models.CharField(max_length=20, default="")

    # def __str__(self):
    #     return self.lifes, self.original_word, self.guessed_word

class Letters(models.Model):
    letters = models.CharField(max_length=1, unique=True)

    # def __str__(self):
    #     return self.letters
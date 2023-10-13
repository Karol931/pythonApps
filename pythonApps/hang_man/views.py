from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import LetterFrom
from utils import hangman
# Create your views here.


def index(request):
    original_word, guessed_word, life_count =  hangman.start()
    template = "hang_man/index.html"
    if request.method == "GET":
        form = LetterFrom()
        context = {
            'lifes' : life_count,
            'word' : guessed_word,
            'form' : form
        } 
        return render(request, template, context)
    if request.method == "POST":
        # Zapisz do bazy danych
        form = LetterFrom(request.POST)
        
        if form.is_valid():
            letter = form.cleaned_data["letter"].lower()
            original_word, guessed_word, life_count = hangman.game(original_word, guessed_word, life_count, letter)
            context = {
                 'lifes' : life_count,
                'word' : guessed_word,
                'form' : form
            }
            return render(request, template, context)

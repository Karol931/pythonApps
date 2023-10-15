from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import LetterFrom
from utils import hangman
from hang_man.models import Game, Letters
# Create your views here.

def process_form(request, form):
    game = Game.objects.get()

    if form.is_valid():
        letter = form.cleaned_data["letter"].lower()
        guessed_letters = Letters.objects.all()
        err_message = ''
        if letter in [l.letters for l in guessed_letters]:
            err_message = f"Can't guess {letter} again"
        else:
            idx = hangman.letter_check(letter, game.original_word)
            if not idx:
                letters = Letters(letters=letter)
                game.lifes -= 1
                game.save()
                letters.save()
            else:
                letters = Letters(letters=letter)
                game.guessed_word = hangman.update_word(indexes=idx, letter=letter, guessed_word=game.guessed_word)
                game.save()
                letters.save()

        return err_message if err_message else None
    else:
        return None

def render_game(request, form, err_message="", end_message=""):
    game = Game.objects.get()
    guessed_letters = Letters.objects.all()
    word = game.guessed_word
    if end_message != '':
        word = game.original_word
    context = {
        'lifes': game.lifes,
        'word': word,
        'form': form,
        'letters': [l.letters for l in guessed_letters],
        'err': err_message,
        'end': end_message,
    }
    return render(request, "hang_man/index.html", context)

def index(request):
    if request.method == "GET":
        Game.objects.all().delete()
        Letters.objects.all().delete()
        original_word, guessed_word, life_count = hangman.start()
        form = LetterFrom()
        game = Game(lifes=life_count, original_word=original_word, guessed_word=guessed_word)
        game.save()
        return render_game(request, form)

    if request.method == "POST":
        form = LetterFrom(request.POST)
        err_message = process_form(request, form)

        if not err_message:
            game = Game.objects.get()

            if game.lifes == 0:
                end_message = 'You lost.'
            elif game.original_word == game.guessed_word:
                end_message = 'You won congratulations!'
            else:
                end_message = ''

            return render_game(request, form, end_message = end_message)

        return render_game(request, form, err_message=err_message)

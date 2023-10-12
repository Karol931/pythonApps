from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    template = "sudoku_solver/index.html"
    sudoku = [
        [5, 0, 0, 0, 0, 0, 0, 8, 1],
        [0, 1, 0, 0, 8, 7, 0, 6, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 5, 0, 0, 6, 1, 0, 7, 0],
        [0, 0, 2, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 0, 0, 4, 0],
        [9, 0, 0, 0, 4, 8, 7, 0, 0],
        [0, 8, 0, 3, 0, 0, 0, 0, 0]
    ]
    context = {
        'sudoku' : sudoku,
    }
    return render(request, template, context)
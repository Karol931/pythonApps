from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from utils import sudoku_solver
# Create your views here.

def index(request):
    template = "sudoku_solver/index.html"
    sudoku = sudoku_solver.create()
    print(sudoku)
    if request.method == "GET":
        context = {
            'sudoku' : sudoku,
            'solvable' : None
        }
        return render(request, template, context)
    elif request.method == "POST":
        is_solvable = sudoku_solver.solver(sudoku)
        print(sudoku)
        context = {
            'sudoku' : sudoku,
            'solvable' : is_solvable
        }
        return render(request, template, context)
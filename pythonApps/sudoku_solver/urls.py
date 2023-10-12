from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="sudoku_solver"),
]
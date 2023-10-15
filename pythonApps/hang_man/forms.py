from django import forms
from django.core.validators import RegexValidator


class LetterFrom(forms.Form):
    alphabet_letters = RegexValidator(r'^[a-zA-Z]', "Only letters are alowed")

    letter = forms.CharField(max_length=1, min_length=1, required=True, validators=[alphabet_letters], label='Guess the letter', initial=None)
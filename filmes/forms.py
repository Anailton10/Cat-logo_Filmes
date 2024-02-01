from django import forms
from .models import FilmRegistration


class MovieForm(forms.ModelForm):

    class Meta:
        model = FilmRegistration
        fields = "__all__"

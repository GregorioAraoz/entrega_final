from django import forms

class formularioanimal(forms.Form):
    especie = forms.CharField(max_length=20)
    alimentacion = forms.CharField(max_length=20)
    
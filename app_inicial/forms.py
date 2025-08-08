from django import forms


class formulariobase(forms.Form):
    especie = forms.CharField(max_length=20)
    alimentacion = forms.CharField(max_length=20)

class formularioanimal(formulariobase): ...
    
class formularioactualizar(formulariobase): ...

class formulariobusqueda(forms.Form):
    especie = forms.CharField(max_length=20, required=False)
    alimentacion = forms.CharField(max_length=20, required=False)
    
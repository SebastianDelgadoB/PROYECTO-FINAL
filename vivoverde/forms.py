from django import forms

class RecetaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    ingredientes = forms.CharField(max_length=200)
    preparacion =forms.CharField(max_length=1000)

class BuscarRecetaForm(forms.Form):
    receta = forms.CharField()

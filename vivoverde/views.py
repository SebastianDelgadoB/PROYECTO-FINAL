from django.shortcuts import render
from .models import Receta
from vivoverde.forms import RecetaFormulario, BuscarRecetaForm

# Create your views here.
def inicio(request):
    return render(request, "index.html")

def receta(request):
    return render(request, "receta.html")

def blog(request):
    return render(request, "blog.html")

def usuario(request):
    return render(request, "usuario.html")

def form_con_api(request):
    if request.method == "POST":
        miFormulario = RecetaFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            receta = Receta(nombre=informacion["receta"], ingredientes=informacion["ingredientes"], preparacion=informacion["preparacion"])

            receta.save()
            return render(request, "vivoverde/index.html")
    else:
        miFormulario = RecetaFormulario()

    return render(request, "vivoverde/form_con_api.html", {"miFormulario": miFormulario})
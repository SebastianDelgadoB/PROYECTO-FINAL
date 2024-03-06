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
        miFormulario = RecetaFormulario(request.POST) 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            receta = Receta(nombre=informacion["receta"], ingredientes=informacion["ingredientes"], preparacion=informacion["preparacion"])

            receta.save()
            return render(request, "vivoverde/index.html")
    else:
        miFormulario = RecetaFormulario()

    return render(request, "vivoverde/form_con_api.html", {"miFormulario": miFormulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        miFormulario = BuscarRecetaForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            receta = Receta.objects.filter(nombre__icontains=informacion["receta"])

            return render(request, "vivoverde/resultados_buscar_form.html", {"recetas": receta})
    else:
        miFormulario = BuscarRecetaForm()

    return render(request, "vivoverde/buscar_form_con_api.html", {"miFormulario": miFormulario})

def mostrar_recetas(request):

    receta = Receta.objects.all()

    contexto= {"recetas": receta} 

    return render(request, "mostrar_recetas.html",contexto)

def crear_receta(request):

    if request.method == "POST":
        miFormulario = RecetaFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            receta = Receta(nombre=informacion["nombre"], ingredientes=informacion["ingredientes"], preparacion=informacion["preparacion"])
            receta.save()
            return render(request, "vivoverde/base.html")
    else:
        miFormulario = RecetaFormulario()

    return render(request, "form_con_api.html", {"miFormulario": miFormulario})
from django.shortcuts import render
from .models import Receta, Blog, Usuario, Administrador
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from vivoverde.forms import RecetaFormulario, BuscarRecetaForm
from django.urls import reverse_lazy


@login_required
def about(request):
    return render(request, "vivoverde/about.html")

def inicio(request):
    return render(request, "index.html")


def receta(request):
    return render(request, "about.html")


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


def buscar_form(request):
    if request.method == "POST":
        miFormulario = BuscarRecetaForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            receta = Receta.objects.filter(nombre__icontains=informacion["receta"])

            return render(request, "buscar_form_con_api.html", {"recetas": receta})
    else:
        miFormulario = BuscarRecetaForm()

    return render(request, "buscar_form_con_api.html", {"miFormulario": miFormulario})


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


def borrar_receta(request,receta_nombre):
    receta = Receta.objects.get(nombre=receta_nombre)
    receta.delete()

    recetas = Receta.objects.all()

    contexto = {"recetas": recetas}

    return render(request, "receta_update.html", contexto)

class RecetaListView(ListView):
    model = Receta
    template_name = "vivoverde/receta_list.html"


class RecetaDetailView(LoginRequiredMixin, DetailView):
    model = Receta
    template_name = "vivoverde/receta_detail.html"
    login_url = '/users/login/'

    def get_login_url(self):
        return self.login_url


class RecetaCreateView(LoginRequiredMixin, CreateView):

    model = Receta
    template_name = "vivoverde/receta_create.html"
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("RecetaList")


class RecetaUpdateView(LoginRequiredMixin, UpdateView):
    model = Receta
    success_url = reverse_lazy("RecetaList")
    fields = ["nombre", "apellido", "email"]
    template_name = "vivoverde/receta_update.html"


class RecetaDeleteView(LoginRequiredMixin, DeleteView):
    model = Receta
    template_name = 'vivoverde/receta_confirm_delete.html'
    success_url = reverse_lazy("RecetaList")




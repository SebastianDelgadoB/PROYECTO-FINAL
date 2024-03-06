from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Receta
from django.urls import reverse_lazy

class RecetaListView(ListView):
    model = Receta
    template_name = "vivoverde/class_list.html"


class RecetaDetailView(DetailView):
    model = Receta
    template_name = "vivoverde/class_detail.html"


class RecetaCreateView(CreateView):

    model = Receta
    template_name = "vivoverde/class_create.html"
    fields = ["nombre", "ingredientes", "preparacion"]

    success_url = reverse_lazy("Administrador")


class RecetaUpdateView(UpdateView):
    model = Receta
    success_url = reverse_lazy("List")
    fields = ["id", "nombre", "ingredientes", "preparacion"]
    template_name = "vivoverde/class_update.html"


class RecetaDeleteView(DeleteView):
    model = Receta
    success_url = reverse_lazy("List")
    template_name = 'vivoverde/class_confirm_delete.html'
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Blog
    template_name = "vivoverde/class_list.html"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "vivoverde/class_detail.html"


class BlogCreateView(CreateView):

    model = Blog
    template_name = "vivoverde/class_create.html"
    fields = ["titulo", "subtitulo", "cuerpo", "autor", "fecha", "imagen"]

    success_url = reverse_lazy("Administrador")


class BlogUpdateView(UpdateView):
    model = Blog
    success_url = reverse_lazy("List")
    fields = ["id", "titulo", "subtitulo", "cuerpo", "autor", "fecha", "imagen"]
    template_name = "vivoverde/class_update.html"


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("List")
    template_name = 'vivoverde/class_confirm_delete.html'
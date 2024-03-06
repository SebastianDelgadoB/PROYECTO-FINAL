from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "index.html")

def recetas(request):
    return render(request, "recetas.html")
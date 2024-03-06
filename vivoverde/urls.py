from django.urls import path
from vivoverde import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('recetas/', views.recetas, name='Recetas'),
]
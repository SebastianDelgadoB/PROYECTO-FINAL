from django.urls import path
from vivoverde import views
from vivoverde import class_views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('recetas/', views.receta, name='Recetas'),
    path('usuarios/', views.receta, name='Usuarios'),
    path('blog/', views.receta, name='Blog'),
    path('about/', views.receta, name='About'),
    path('form-con-api/', views.form_con_api, name="Form-Con-Api"),
    path('buscar-form/', views.buscar_form, name="Buscar-Form"),
    path('mostrar-recetas/', views.mostrar_recetas, name="Mostrar-Recetas"),
    path('crear-receta/', views.crear_receta, name="Crear-Receta"),
    path('borrar-receta/', views.borrar_receta, name="Borrar-Receta"),
]

# URL's basadas en clases
urlpatterns += [
    path('receta-list/', class_views.RecetaListView.as_view(), name="RecetaList"),
    path('receta-detail/<pk>/', class_views.RecetaDetailView.as_view(), name="RecetaDetail"),
    path('receta-create/', class_views.RecetaCreateView.as_view(), name="RecetaCreate"),
    path('receta-update/<pk>/', class_views.RecetaUpdateView.as_view(), name="RecetaUpdate"),
    path('receta-delete/<pk>/', class_views.RecetaDeleteView.as_view(), name="RecetaDelete"),
]
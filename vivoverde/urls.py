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
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar-Form-Con-Api"),
    path('mostrar-recetas/', views.mostrar_recetas, name="Mostrar_Recetas"),
    path('crear_receta/', views.crear_receta, name="CrearReceta"),
]

# URL's basadas en clases
urlpatterns += [
    path('class-list/', class_views.RecetaListView.as_view(), name="List"),
    path('class-detail/<pk>/', class_views.RecetaDetailView.as_view(), name="Detail"),
    path('class-create/', class_views.RecetaCreateView.as_view(), name="Create"),
    path('class-update/<pk>/', class_views.RecetaUpdateView.as_view(), name="Update"),
    path('class-delete/<pk>/', class_views.RecetaDeleteView.as_view(), name="Delete"),
]
from django.urls import path
from vivoverde import views
from vivoverde import class_views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('recetas/', views.recetas, name='Recetas'),
    path('usuarios/', views.recetas, name='Usuarios'),
    path('blog/', views.recetas, name='Blog'),
    path('form-con-api/', views.form_con_api, name="Form-Con-Api"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar-Form-Con-Api"),
    path('mostrar-recetas/', views.mostrar_recetas, name="Mostrar_Cursos"),
]

# URL's basadas en clases
urlpatterns += [
    path('class-list/', class_views.BlogListView.as_view(), name="List"),
    path('class-detail/<pk>/', class_views.BlogDetailView.as_view(), name="Detail"),
    path('class-create/', class_views.BlogCreateView.as_view(), name="Create"),
    path('class-update/<pk>/', class_views.BlogUpdateView.as_view(), name="Update"),
    path('class-delete/<pk>/', class_views.BlogDeleteView.as_view(), name="Delete"),
]
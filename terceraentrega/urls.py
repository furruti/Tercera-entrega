# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('crear-autor/', views.crear_autor, name='crear_autor'),
    path('buscar-autor/', views.buscar_autor, name='buscar_autor'),
]

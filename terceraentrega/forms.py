from django import forms
from .models import Autor, Libro, Editorial

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre del autor'}),
            'nacionalidad': forms.TextInput(attrs={'placeholder': 'Nacionalidad del autor'}),
        }

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Título del libro'}),
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la editorial'}),
            'ubicacion': forms.TextInput(attrs={'placeholder': 'Ubicación de la editorial'}),
        }

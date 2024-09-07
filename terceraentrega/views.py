from django.shortcuts import render, redirect
from .forms import AutorForm, LibroForm, EditorialForm

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autores')
    else:
        form = AutorForm()
    return render(request, 'crear_autor.html', {'form': form})

def buscar_autor(request):
    autores = None
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        autores = Autor.objects.filter(nombre__icontains=nombre)
    return render(request, 'buscar_autor.html', {'autores': autores})

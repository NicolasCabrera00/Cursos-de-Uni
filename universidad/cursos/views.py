from email import message
from django.shortcuts import redirect, render
from .models import Curso
from django.contrib import messages

def home(request):
    return render(request, 'base.html')
    


def gestion(request):
    curso = Curso.objects.all()
    return render(request,'gestion_cursos.html', {'curso': curso})



def registrarCurso(request):
    """ Guardo los datos obtenidos en el formulario """
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    nota = request.POST['txtNota']
    
    """ Creo un nuevo objeto con los datos guardados """
    curso = Curso.objects.create(codigo = codigo, nombre = nombre,nota = nota)

    messages.success(request, 'Curso registrado')
    return redirect('/gestion')

def eliminar(request, codigo):
    curso = Curso.objects.get(codigo = codigo)
    curso.delete()
    messages.success(request, 'Curso elminado')
    return redirect('/gestion')

def formEditar(request, codigo):
    curso = Curso.objects.get(codigo = codigo)
    nombre = curso.nombre
    codigo = curso.codigo
    
    return render(request, 
                  'formEditar.html', 
                  {'codigo': codigo,
                   'curso': nombre})

def guardarEdicion(request):
    """ Guardo los datos obtenidos en el formulario """
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    nota = request.POST['txtNota']
    
    curso = Curso.objects.get(codigo = codigo)

    """ Todo lo recibido desde el formulario se remplaza en el objeto original """
    curso.codigo = codigo
    curso.nombre = nombre
    curso.nota = nota

    messages.success(request, 'Curso guardado')
    curso.save()

    return redirect('/')

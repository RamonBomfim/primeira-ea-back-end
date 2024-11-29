from django.shortcuts import render
from .models import Aluno, Curso

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'alunos/lista_cursos.html', {'cursos': cursos})


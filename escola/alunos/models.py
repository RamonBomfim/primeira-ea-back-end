from django.db import models

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    
    cursos = models.ManyToManyField(Curso, related_name='alunos')

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.aluno} - {self.curso}"
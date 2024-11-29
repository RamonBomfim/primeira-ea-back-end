from django.contrib import admin
from .models import Aluno, Curso

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'curso')  # Exibir curso no admin
    list_filter = ('curso',)

admin.site.register(Aluno)
admin.site.register(Curso)
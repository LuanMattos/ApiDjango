from django.contrib import admin
from escola.models import Aluno, Curso

class Alunos(admin.ModelAdmin):
    list_display = ('id','nome','rg','cpf','data_nascimento')
    list_display_link = ('id','nome')
    list_per_page = 20
    search_fields = ('nome',)

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id','codigo_curso','descricao')
    list_display_link = ('id','codigo_curso')
    list_per_page = 20
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)


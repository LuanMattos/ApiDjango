from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer ,ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosCursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibe todos os alunos """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """ Exibe todos os cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """ Lista todas as matrículas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    """Lista as matrículas de um Aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListCreateAPIView):
    """ Lista alunos matriculados em um curso - neste query set que pegamos o pk da requisição """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosCursoSerializer
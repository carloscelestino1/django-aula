from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm
from  django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def alunoView(request):
    alunos_list = Aluno.objects.all().order_by('-created_at').filter(user=request.user)

    paginator = Paginator(alunos_list, 5)

    page = request.GET.get('page')
    tasks = paginator.get_page(page)


    return render(request, 'main/list.html', {'alunos':tasks})


@login_required
def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    return render(request, 'main/aluno.html', {'aluno': aluno})

@login_required
def newAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.status = 'ativo'
            aluno.user = request.user
            aluno.save()
            return redirect('/')
    else:
        form = AlunoForm()
    return render(request, 'main/add_aluno.html', {'form': form})
@login_required
def editAluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    form = AlunoForm(instance=aluno)

    if(request.method == 'POST'):
        form = AlunoForm(request.POST, instance=aluno)

        if(form.is_valid()):
            aluno.save()
            return redirect('/')
        else:
            return render(request, 'main/edit_aluno.html', {'form': form, 'aluno': aluno})
    else:
        return render(request, 'main/edit_aluno.html', {'form': form, 'aluno': aluno})
@login_required
def deleteAluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    aluno.delete()
    return redirect('/')


from .serializers import EventoSerializer
from rest_framework import viewsets

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = EventoSerializer
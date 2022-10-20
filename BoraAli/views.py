from django.shortcuts import get_object_or_404, redirect, render
from .models import Trilha
from .forms import TrilhaForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django

# from email import message
# from email.message import Message
# from pyexpat.errors import messages

# Create your views here.


def index(request):
    trilhas = Trilha.objects.all()

    dados = {
        'trilhas': trilhas
    }
    return render(request, 'index.html', dados)


def trilha(request, trilha_id):
    trilha = get_object_or_404(Trilha, pk=trilha_id)

    trilha_a_exibir = {
        'trilha': trilha
    }

    return render(request, 'trilha.html', trilha_a_exibir)


def trilha_add(request):
    # return render(request, 'trilha_add.html')
    if request.method == "GET":
        return render(request, 'trilha_add.html')
    else:
        nome_trilha = request.POST.get('nome_trilha')
        descricao = request.POST.get('descricao')
        localizacao = request.POST.get('localizacao')
        duracao = request.POST.get('duracao')
        nivel = request.POST.get('nivel')
        curiosidades = request.POST.get('curiosidades')

        trilha = Trilha(nome_trilha=nome_trilha, descricao=descricao, localizacao=localizacao,
                        duracao=duracao, nivel=nivel, curiosidades=curiosidades)

        trilha.save()
        # messages.info(request, 'Trilha cadastrada com sucesso')
        return redirect('modificacao')

def trilha_del(request, trilha_id):
    trilha = get_object_or_404(Trilha, pk=trilha_id)
    trilha.delete()
    return redirect('modificacao')



def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user:
            login_django(request, user)
            return render(request, 'index.html')
        else:
            return redirect('login')


def logout(request):
    logout_django(request)
    return render(request, 'index.html')


def modificacao(request):
    trilhas = Trilha.objects.all()

    dados = {
        'trilhas': trilhas
    }
    return render(request, 'modificacao.html', dados)


def trilha_edit(request,trilha_id):
    trilha = get_object_or_404(Trilha,pk=trilha_id)

    form = TrilhaForm(request.POST or None, instance=trilha)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('modificacao')
    
    context = {
        'trilha' : trilha.id,
        'form' : form,
    }

    return render (request, 'modificacao', context)
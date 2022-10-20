from email import message
from email.message import Message
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Trilha

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

        trilha = Trilha(nome_trilha=nome_trilha, descricao=descricao, localizacao=localizacao,duracao=duracao, nivel=nivel, curiosidades=curiosidades)

        trilha.save()
        # messages.info(request, 'Trilha cadastrada com sucesso')
        return redirect('index')

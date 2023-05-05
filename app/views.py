from django.shortcuts import render

from django.http import HttpResponse

from .models import Usuario

# Create your views here.


def index(request):

   return render(request,'usu/home.html')

def infor(request):
    #salva os dados da tela no banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # agora preciso exibir todos usu no banco de dados

   # tem que se rum dicionario
    infor = {
       'infor': Usuario.objects.all()
   }

    #listagem de usuarios 

    return render(request,'mais/info.html',infor)
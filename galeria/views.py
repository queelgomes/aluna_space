from django.shortcuts import render
## from django.http import HttpResponse >>> esse usa quando for colocar o html dentro das aspas aqui mesmo. Nao reocomendado.

def index(request): # aqui vai solicitar o requerimento e vai retornar essa=e httpresponse. Colocar na pasta urls em setup
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')
from django.shortcuts import render
import markdown 
import requests 

from datetime import datetime

def calcular_idade(data_nascimento):
    hoje = datetime.now()
    data_nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
    
    aniversario_ocorrido = (hoje.month, hoje.day) >= (data_nascimento.month, data_nascimento.day)

    idade = hoje.year - data_nascimento.year - (not aniversario_ocorrido)
    
    return idade

def home(request):
    return render(request, 'home.html')
def projetos(request):
    return render(request, 'projetos.html')
def info(request):
    data_nascimento = "2003-07-24"
    idade = calcular_idade(data_nascimento)
    context = {
        'idade' : idade,
    }
    return render(request, 'info.html', context)
def crypto(request):
    return render(request, 'info.html')
def sistema(request):
    return render(request, 'sistema.html')
def contato(request):
    return render(request, 'info.html')

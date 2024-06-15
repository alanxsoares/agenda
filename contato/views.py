from django.shortcuts import render
from contato.models import Contato

def index(request):
    consulta = Contato.objects.all()[10:30]
    context ={
        'consulta':consulta
    }
    
    return render(request, 'index.html', context)

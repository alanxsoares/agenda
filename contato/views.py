from django.shortcuts import render
from django.core.paginator import Paginator
from contato.models import Contato


def index(request):

    consulta = Contato.objects.all()  # pyright: ignore
    pagina = Paginator(consulta, 15)
    pnum = request.GET.get('page')
    page = pagina.get_page(pnum)
    return render(request, 'index.html', {'page': page})


def show_contato(request, contato_id):

    contato = Contato.objects.get(pk=contato_id)
    context = {'contato': contato}

    return render(request, 'show_contato.html', context)

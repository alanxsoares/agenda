from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from contato.forms import ContatoModelForm
from contato.models import Contato
from django.db.models import Q

app_name = "contato"


def index(request):

    consulta = Contato.objects.filter(show=True)\
        .order_by('-id')  # pyright: ignore
    pagina = Paginator(consulta, 15)
    pnum = request.GET.get('page')
    page = pagina.get_page(pnum)
    return render(request, 'index.html', {'page': page})


def show_contato(request, contato_id):

    contato = Contato.objects.get(pk=contato_id)  # pyright: ignore
    context = {'contato': contato}

    return render(request, 'show_contato.html', context)


def search(request):
    q_value = request.GET.get('q', '').strip()

    if q_value == '':

        return redirect('contato:index')

    consulta = Contato.objects \
        .filter(show=True)\
        .filter(
            Q(nome__icontains=q_value)  # pyright: ignore
            | Q(sobrenome__icontains=q_value)
            | Q(email__icontains=q_value)
            | Q(telefone__icontains=q_value)
        )\
        .order_by('-id')
    pagina = Paginator(consulta, 15)
    pnum = request.GET.get('page')
    page = pagina.get_page(pnum)
    return render(request, 'index.html', {'page': page, 'q_value': q_value})


def add_contato(request):
    if request.method == 'POST':
        form = ContatoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contato:index')
        else:
            return render(request, 'form_contato.html', {'form': form})

    else:
        form = ContatoModelForm
        return render(request, 'create.html', {'form': form})


def up_contato(request, pk):

    contato = get_object_or_404(Contato, pk=pk)
    if request.method == 'POST':
        form = ContatoModelForm(request.POST, request.FILES, instance=contato)
        if form.is_valid():
            form.save()
            return redirect('contato:index')
        else:
            return render(request, 'form_contato.html', {'form': form})

    else:
        form = ContatoModelForm(instance=contato)
        return render(request, 'form_contato.html', {'form': form})

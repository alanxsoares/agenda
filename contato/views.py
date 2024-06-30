from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import auth
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from contato.forms import ContatoModelForm, UserRegisterForm
from contato.models import Contato
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

app_name = "contato"


def index(request):

    consulta = Contato.objects.filter(show=True).order_by('-id')
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


@login_required(login_url='contato:login')
def add_contato(request):
    if request.method == 'POST':
        form = ContatoModelForm(request.POST, request.FILES)
        if form.is_valid():
            contato = form.save(commit=False)
            contato.criador = request.user
            form.save()
            messages.success(request, 'Contato adicionado com sucesso')
            return redirect('contato:index')
        else:
            return render(request, 'form_contato.html', {'form': form})

    else:
        form = ContatoModelForm
        return render(request, 'form_contato.html', {'form': form})


@login_required(login_url='contato:login')
def up_contato(request, pk):
    contato = get_object_or_404(Contato, pk=pk,
                                show=True, criador=request.user)
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


@login_required(login_url='contato:login')
def del_contato(request, pk):
    contato = get_object_or_404(
        Contato, pk=pk, show=True, criador=request.user)

    contato.delete()
    messages.success(request, 'Contato excluido com sucesso')
    return redirect('contato:index')


def user_create(request):
    form = UserRegisterForm()
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario Criado com sucesso ')
            return redirect('contato:login')

    return render(request, 'form_user.html', {'form': form})


def user_login(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login feito com sucesso')
            return redirect('contato:index')
        messages.error(request, 'login invalido!')

    return render(request, 'user_login.html', {'form': form})


@login_required(login_url='contato:login')
def user_logout(request):
    auth.logout(request)
    return redirect('contato:index')

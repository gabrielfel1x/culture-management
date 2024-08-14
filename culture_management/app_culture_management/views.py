from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from .forms import EventoForm, SignUpForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()

    return render(request, 'app_culture_management/(auth)/signin/index.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'app_culture_management/(auth)/signup/index.html', {'form': form})


def home(request):
    eventos = Evento.objects.all()
    return render(request, 'app_culture_management/dashboard/home.html', {'eventos': eventos})

def relatorios(request):
    return render(request, 'app_culture_management/dashboard/relatorios.html')

def configuracoes(request):
    return render(request, 'app_culture_management/dashboard/configuracoes.html')

def perfil(request):
    return render(request, 'app_culture_management/dashboard/perfil.html')

# parte de eventos

def listar_eventos(request):
    eventos = Evento.objects.all()
    form = EventoForm()  # Instancia o formulário aqui
    return render(request, 'app_culture_management/dashboard/eventos/eventos.html', {'eventos': eventos, 'form': form})


def detalhes_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'app_culture_management/dashboard/eventos/detalhes_evento.html', {'evento': evento})

def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            print("Formulário é válido")
            form.save()
            return redirect('listar_eventos')
        else:
            print("Formulário não é válido", form.errors)
    else:
        form = EventoForm()
    
    return render(request, 'app_culture_management/dashboard/eventos/criar_evento.html', {'form': form})

def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('listar_eventos')
    else:
        data = {
            'titulo': evento.titulo,
            'tipo': evento.tipo,
            'data': evento.data,
            'horario': evento.horario,
            'local': evento.local,
            'cidade': evento.cidade,
            'valor': evento.valor,
            'entrada_gratuita': evento.entrada_gratuita,
            'vagas': evento.vagas,
        }
        return JsonResponse(data)


def deletar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('listar_eventos')
    return render(request, 'app_culture_management/dashboard/eventos/deletar_evento.html', {'evento': evento})

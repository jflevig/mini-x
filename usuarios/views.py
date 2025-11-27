from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Perfil


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not user.perfil.biografia:
                return redirect(reverse_lazy('editar_perfil'), kwargs={'pk': user.pk})
            return redirect(reverse_lazy('home'))
        return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('login'))


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Perfil.objects.create(usuario=usuario)

            return redirect(reverse_lazy('login'))
        
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form})


def perfil(request, pk):
    perfil = Perfil.objects.get(usuario__pk=pk)
    posts = perfil.usuario.posts.all().order_by('-created_at')
    return render(request, 'perfil.html', {'perfil': perfil, 'posts': posts})


def editar_perfil(request):
    perfil = Perfil.objects.get(usuario=request.user)

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        biografia = request.POST.get('biografia', '')
        email = request.POST.get('email', '')
        perfil.nombre = nombre
        perfil.biografia = biografia
        perfil.save()
        perfil.usuario.email = email
        perfil.usuario.save()
        return redirect(reverse_lazy('perfil', kwargs={'pk': request.user.pk}))

    return render(request, 'editar_perfil.html', {'perfil': perfil})



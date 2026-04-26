from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'app/dashboard.html')

@login_required
def logs(request):
    return render(request, 'app/logs.html')

@login_required
def settings_view(request):
    return render(request, 'app/settings.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'app/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

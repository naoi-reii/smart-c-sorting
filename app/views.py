from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import UserProfile

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

@login_required
def update_username(request):
    if request.method == 'POST':
        new_username = request.POST.get('username')
        if new_username:
            request.user.username = new_username
            request.user.save()
            messages.success(request, "Username updated.")
    
    response = render(request, 'app/settings.html')
    response['HX-Trigger'] = 'modalClose'
    return response

@login_required
def update_email(request):
    if request.method == 'POST':
        new_email = request.POST.get('email')
        if new_email:
            request.user.email = new_email
            request.user.save()
            messages.success(request, "Email updated.")
            
    response = render(request, 'app/settings.html')
    response['HX-Trigger'] = 'modalClose'
    return response

@login_required
def update_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        
        if request.user.check_password(current_password) and new_password:
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)  # Keep user logged in
            messages.success(request, "Password updated.")
            
    response = render(request, 'app/settings.html')
    response['HX-Trigger'] = 'modalClose'
    return response

@login_required
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        profile.image = request.FILES['image']
        profile.save()
        
    response = render(request, 'app/settings.html')
    response['HX-Trigger'] = 'modalClose'
    return response

@login_required
def remove_image(request):
    if request.method == 'POST':
        try:
            profile = request.user.userprofile
            if profile.image:
                profile.image.delete(save=False)
                profile.image = None
                profile.save()
        except UserProfile.DoesNotExist:
            pass
            
    response = render(request, 'app/settings.html')
    response['HX-Trigger'] = 'modalClose'
    return response

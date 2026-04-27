from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import UserProfile, Device
import json

# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'app/dashboard.html')

@login_required
def logs(request):
    return render(request, 'app/logs.html')

@login_required
def diagnostics(request):
    return render(request, 'app/diagnostics.html')

@login_required
def diagnostics_status(request):
    # Check for Orange Pi device
    device, created = Device.objects.get_or_create(name="Orange Pi")
    
    # Consider "Online" if seen in the last 15 seconds
    is_online = False
    if device.last_seen:
        diff = timezone.now() - device.last_seen
        if diff.total_seconds() < 15:
            is_online = True
            
    return render(request, 'app/partials/diagnostic_status.html', {
        'device': device,
        'is_online': is_online
    })

@csrf_exempt
def api_ping(request):
    if request.method == 'POST':
        try:
            # We don't necessarily need body data for a simple ping, 
            # but we can capture the sender's IP.
            device, created = Device.objects.get_or_create(name="Orange Pi")
            
            # Update IP and timestamp
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
                
            device.ip_address = ip
            device.save() # auto_now will update last_seen
            
            return JsonResponse({"status": "ok", "timestamp": timezone.now()}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    
    return JsonResponse({"status": "ignored"}, status=405)

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

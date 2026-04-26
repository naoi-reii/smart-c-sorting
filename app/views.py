from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'app/dashboard.html')

def logs(request):
    return render(request, 'app/logs.html')

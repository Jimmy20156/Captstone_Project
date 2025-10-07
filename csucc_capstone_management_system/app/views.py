from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'public/index.html')

def login(request):
    return render(request, 'public/login.html')

def register(request):
    return render(request, 'public/register.html')

def dashboard(request):
    return render(request, 'public/student_dashboard.html')

def features(request):
    return render(request, 'public/features.html')

def projects(request):
    return render(request, 'public/projects.html')

def support(request):
    return render(request, 'public/support.html')
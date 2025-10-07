from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, SignInForm

#decorators 
from django.contrib.auth.decorators import login_required

# deafult login form 
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
    return render(request, 'public/index.html')

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # 👇 Respect ?next= parameter
            next_url = request.POST.get('next') or request.GET.get('next') or '/dashboard/'
            return redirect(next_url)
    else:
        form = AuthenticationForm()

    # 👇 Pass the ?next= value to the template
    return render(request, 'public/test_login.html', {
        'form': form,
        'next': request.GET.get('next', ''),
    })


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or wherever you want to go next
    else:
        form = SignUpForm()
    return render(request, 'public/test_register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'public/student_dashboard.html')


def features(request):
    return render(request, 'public/features.html')

def projects(request):
    return render(request, 'public/projects.html')

def support(request):
    return render(request, 'public/support.html')
def signout(request):
    logout(request)
    return render(request, 'public/index.html')

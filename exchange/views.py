from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exchange:login')
    else:
        form = SignUpForm()
    return render(request, 'exchange/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('exchange:home')
    else:
        form = LoginForm()
    return render(request, 'exchange/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('exchange:login')

@login_required
def home_view(request):
    return render(request, 'exchange/home.html')
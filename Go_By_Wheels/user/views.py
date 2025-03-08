from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})

def dashboard(request):
    if request.user.role == 'driver':
        return redirect('driver_dashboard')
    elif request.user.role == 'mechanic':
        return redirect('mechanic_dashboard')
    return render(request, 'user/dashboard.html')

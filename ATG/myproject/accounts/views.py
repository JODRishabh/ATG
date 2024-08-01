from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import User
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.user_type == 'patient':
                return redirect('patient_dashboard')
            else:
                return redirect('doctor_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html')


from django.shortcuts import render

def home(request):
    return render(request, 'accounts/home.html')




def custom_logout_view(request):
    logout(request)
    return redirect('login')

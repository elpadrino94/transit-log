from django.shortcuts import redirect, render

from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

from account.forms import CustomUserCreationForm
from account.models import CustomUser

# Create your views here.

#=================
#    LOGIN VIEWS
#=================

def login_view(request):
    # Si user est déjà authentifié
    if request.user.is_authenticated:
        if getattr(request.user, 'role', None) == 'admin':
            return redirect('dashboard-home')
        return redirect('home')  
    
    if request.method == 'POST':
        # Handle login form submission
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # Redirect based on user role 
            if user.role == 'admin':
                return redirect('dashboard-home')
            else:
                return redirect('home')  # Redirect to a success page
        else:
            # Invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid email or password.'})
        
    return render(request, 'login.html')


#==============
# SIGNUP VIEW
#==============
def register_view(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'register.html', {'form': form})



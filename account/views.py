from django.shortcuts import redirect, render

from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#=================
#    LOGIN VIEWS
#=================

def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a success page
        else:
            # Invalid login credentials
            return render(request, 'account/login.html', {'error': 'Invalid email or password.'})
    return render(request, 'login.html')



from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password

def signup(request):
    if request.method == 'POST':
        if request.POST.get('password1')==request.POST.get('password2'):
            try:
                User.objects.get(username=request.POST.get('username'))
                return render(request, 'accounts/signup.html', {'error': 'Username already taken'})
            except User.DoesNotExist:
                password = make_password(request.POST.get('password1'))
                user = User.objects.create(username=request.POST.get('username'), password=password)
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password must match'})
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        password = make_password(request.POST.get('password1'))
        user = auth.authenticate(username=request.POST['username'], password=request.POST.get('password1'))
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')



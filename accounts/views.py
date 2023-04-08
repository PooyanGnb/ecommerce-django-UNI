from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from accounts.forms import SignUpForm, LoginForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                try:
                    user = User.objects.get(email=username)
                    if not user.check_password(password):
                        user = None
                except ObjectDoesNotExist:
                    user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        return render(request, 'accounts/login.html')
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
    

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.clean()
                try:
                    form.save()
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password1')
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('/')
                except IntegrityError:
                    pass
    return render(request, 'accounts/signup.html')
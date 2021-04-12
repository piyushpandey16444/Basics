from django.shortcuts import render
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm


def signup_view(request):
    """
    for user registration
    """
    if request.method == "GET":
        form = CreateUserForm()

    elif request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully !')
            form = CreateUserForm()

    context = {
        'form': form,
    }
    return render(request, 'enroll/signup.html', context)


def login_view(request):
    """
    for user login and redirection
    """
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
            else:
                pass
    return render(request, 'enroll/login.html', {"form": form})


def profile_view(request):
    return render(request, 'enroll/profile.html')

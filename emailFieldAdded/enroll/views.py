from django.shortcuts import render
from .forms import CreateUserForm
from django.contrib import messages


def signup_view(request):

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

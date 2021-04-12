from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def signup_view(request):

    if request.method == "GET":
        form = UserCreationForm()

    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'enroll/signup.html', context)

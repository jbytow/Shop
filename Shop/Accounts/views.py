from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import CreateUserForm


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was successfully created')
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

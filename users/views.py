from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required #декоратор против анонимного пользователя

from users.forms import UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('shortener:general'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы усепешно зарегестрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('shortener:index'))

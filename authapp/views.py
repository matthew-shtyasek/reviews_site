from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import LoginForm, SingInForm


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            auth.login(request=request, user=login_form.get_user())
            return HttpResponseRedirect(reverse('main:index'))
    else:
        login_form = LoginForm()

    context = {
        'page_title': 'авторизация',
        'submit_title': 'войти',
        'form': login_form
    }
    return render(request, template_name='authapp/authentication.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def sing_in(request):
    if request.method == 'POST':
        sing_in_form = SingInForm(data=request.POST)
        if sing_in_form.is_valid():
            sing_in_form.save()
            return HttpResponseRedirect(reverse('auth:login_page'))
    else:
        sing_in_form = SingInForm()
    context = {
        'page_title': 'регистрация',
        'submit_title': 'зарегистрироваться',
        'is_login': False,
        'form': sing_in_form,
    }
    return render(request, template_name='authapp/authentication.html', context=context)

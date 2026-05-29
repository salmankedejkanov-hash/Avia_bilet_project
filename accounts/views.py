from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.decorators import login_required


class CustomLoginView(LoginView):

    template_name = 'accounts/login.html'


class CustomLogoutView(LogoutView):

    next_page = '/'


def register_view(request):

    form = UserCreationForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect(
            'login'
        )

    context = {
        'form': form
    }

    return render(
        request,
        'accounts/register.html',
        context
    )


@login_required
def profile_view(request):

    return render(
        request,
        'accounts/profile.html'
    )
from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.decorators import login_required

from .forms import RegisterForm


class CustomLoginView(LoginView):

    template_name = 'accounts/login.html'


class CustomLogoutView(LogoutView):

    next_page = '/'


def register_view(request):

    form = RegisterForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect(
            'login'
        )

    context = {
        'form': form
    }

    return render(
        request,
        'accounts/register.html',
        context
    )


@login_required
def profile_view(request):

    return render(
        request,
        'accounts/profile.html'
    )

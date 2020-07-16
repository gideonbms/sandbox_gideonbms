from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import EmployeeRegistrationForm


def signup(request):
    next = request.GET.get('next')
    form = EmployeeRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('accounts:login')

    context = {
        'form': form,
    }

    return render(request, "accounts/employee_signup.html", context)



def logout_view(request):
    logout(request)
    return redirect('accounts:login')

def logform(request):
    form = LogForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return redirect('jobs:experiment')
    context = {
        'form': form
    }
    return render(request, "accounts/login.html", context)
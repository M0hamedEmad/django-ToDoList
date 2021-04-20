from django.shortcuts import render, redirect
from .form import UserregisterionForm
from django.contrib.auth import authenticate, login, logout
from .decorators import is_unauthenticate

@is_unauthenticate
def register(request):
    """Create a new account"""
    form = UserregisterionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form':form,
    }
    return render(request, 'account/register.html', context)

@is_unauthenticate
def loginPage(request):
    """ login a user """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if authenticate is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'account/login.html')
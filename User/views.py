from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignupForm


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'User/signup.html'
    # success_url = reverse_lazy('home')


def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Such a user does not exist')
            return redirect('Users:login')
    return render(request, 'User/login.html')


@login_required
def logOut(request):
    logout(request)
    return redirect('home')


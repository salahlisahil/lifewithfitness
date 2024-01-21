from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import forms
from django.shortcuts import render, redirect
from django.views import View

from gym.forms import LoginForm, RegistrationForm


class LoginView(View):
    template_name = 'auth/register.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error('email', forms.ValidationError("User with this credentials doesn't exist"))
                return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})


class RegisterView(View):
    template_name = 'auth/register.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

        return render(request, self.template_name, {'form': form})


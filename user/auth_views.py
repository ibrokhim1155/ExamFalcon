from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from user.forms import AddUserForm
from django.contrib.auth.forms import AuthenticationForm

class RegisterView(View):
    template_name = 'auth/register.html'

    def get(self, request, *args, **kwargs):
        form = AddUserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            send_mail(
                'User Successfully Registered',
                'Welcome to our platform!',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False
            )
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('customer_list')
        else:
            messages.error(request, "Invalid registration details.")
        return render(request, self.template_name, {'form': form})

class LoginView(View):
    template_name = 'auth/login.html'

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                messages.info(request, f"You are now logged in as {email}.")
                return redirect('customer_list')
            else:
                messages.error(request, "Invalid email or password.")
        return render(request, self.template_name, {'form': form})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect('customer_list')

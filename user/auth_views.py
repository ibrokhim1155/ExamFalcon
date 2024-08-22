from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user.forms import AddUserForm, SendingEmailForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings
from django.views import View


def register(request):
    if request.method == 'POST':
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
            print(form.errors)
    else:
        form = AddUserForm()
    return render(request, 'auth/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            messages.info(request, f"You are now logged in as {email}.")
            return redirect('customer_list')
        else:
            messages.error(request, "Invalid email or password.")

    form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('customer_list')


class SendingEmail(View):
    sent = False

    def get(self, request, *args, **kwargs):
        form = SendingEmailForm()
        context = {
            'form': form,
            'sent': self.sent
        }
        return render(request, 'users/send-email.html', context)

    def post(self, request, *args, **kwargs):
        form = SendingEmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_list = form.cleaned_data['recipient_list']
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                recipient_list,
                fail_silently=False
            )
            self.sent = True
            context = {
                'form': form,
                'sent': self.sent
            }
            return render(request, 'users/send-email.html', context)
        else:
            context = {
                'form': form,
                'sent': self.sent
            }
            return render(request, 'users/send-email.html', context)

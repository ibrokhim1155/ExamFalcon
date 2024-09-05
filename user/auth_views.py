from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth.tokens import default_token_generator
from user.forms import RegisterModelForm
from user.tokens import account_activation_token

class RegisterPage(FormView):
    template_name = 'users/auth/register.html'
    form_class = RegisterModelForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        # Email activation
        current_site = get_current_site(self.request)
        message = render_to_string('users/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        email = EmailMessage(
            'Activate your account',
            message,
            settings.EMAIL_DEFAULT_SENDER,
            [user.email],
        )
        email.content_subtype = 'html'
        email.send()

        return super().form_valid(form)

def activate_account(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=uid)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Your account has been activated!')
            return redirect('login')
        else:
            messages.error(request, 'Activation link is invalid!')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, 'Activation link is invalid!')
    return redirect('register')

class LoginView(View):
    template_name = 'users/auth/login.html'

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
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
        return redirect('login')

class SendingEmail(View):
    def get(self, request, *args, **kwargs):

        return HttpResponse('Email sent!')

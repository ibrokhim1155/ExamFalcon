from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import render
from django.core.mail import send_mail
from user.forms import SendingEmailForm
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages

def active(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated successfully.')
        return redirect('login')  # Redirect to login page after activation
    else:
        messages.error(request, 'The activation link is invalid or has expired.')
        return HttpResponse('Activation link is invalid or expired.')

class SendingEmail(View):
    template_name = 'users/send-email.html'
    sent = False

    def get(self, request, *args, **kwargs):
        form = SendingEmailForm()
        context = {
            'form': form,
            'sent': self.sent
        }
        return render(request, self.template_name, context)

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
        return render(request, self.template_name, context)

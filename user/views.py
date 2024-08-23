from django.shortcuts import render

# Create your views here.
from django.views import View
from django.shortcuts import render
from django.core.mail import send_mail
from user.forms import SendingEmailForm
from django.conf import settings

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

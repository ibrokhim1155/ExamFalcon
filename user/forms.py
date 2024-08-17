from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User



class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))

    class Meta:
        model = User
        fields = ['email', 'password']

from django import forms
from user.models import User



class AddUserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, max_length=100)
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords must match')
        return password

    def save(self, commit=True):
        user = super(AddUserForm, self).save(commit=False)
        user.set_password(self.data.get('password'))
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user



# class CustomAuthenticationForm(AuthenticationForm):
#     username = forms.EmailField(label="Email", max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
#
#     class Meta:
#         model = User
#         fields = ['email', 'password']

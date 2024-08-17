from django import forms
from .models import Customer
from django.contrib.auth.models import User

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

#
# class AddUserForm(forms.ModelForm):
#     confirm_password = forms.CharField(widget=forms.PasswordInput, max_length=100)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
#     def clean_password(self):
#         password = self.data.get('password')
#         confirm_password = self.data.get('confirm_password')
#         if password != confirm_password:
#             raise forms.ValidationError('Passwords must match')
#         return password
#
#     def save(self, commit=True):
#         user = super(AddUserForm, self).save(commit=False)
#         user.set_password(self.data['password'])
#         user.is_superuser = True
#         user.is_staff = True
#
#         if commit:
#             user.save()
#
#         return user
#
#
# class AuthenticationForm(forms.Form):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

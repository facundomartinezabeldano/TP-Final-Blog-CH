from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserSignInForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(
        required=True, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        required=True, label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {k: "" for k in fields}

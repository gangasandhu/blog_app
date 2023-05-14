from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from users.models import Profile

field_style = 'form-control border border-purple-300 bg-gray-50 text-gray-900 sm:text-sm rounded-lg focus:ring-2 focus:ring-purple-300 focus:border-transparent block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': field_style, 'placeholder': 'email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = field_style
        self.fields['username'].widget.attrs['placeholder'] = 'username'

        self.fields['password1'].widget.attrs['class'] = field_style
        self.fields['password1'].widget.attrs['placeholder'] = 'password'

        self.fields['password2'].widget.attrs['class'] = field_style
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm password'

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': field_style, 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': field_style, 'placeholder': 'password'}))


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email',]

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = field_style
        self.fields['email'].widget.attrs['class'] = field_style


class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['avatar']
        
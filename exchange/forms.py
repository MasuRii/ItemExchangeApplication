from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .models import User

class SignUpStep1Form(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'required': True}))
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'required': True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True}))


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
        return cleaned_data
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email


class SignUpStep2Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'city', 'state', 'country', 'zip_code', 'terms_agreed']

        widgets = {
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': True}),
            'terms_agreed': forms.CheckboxInput(attrs={'required': True}),
        }

        labels = {
            'terms_agreed': 'I agree to the <a href="/terms/" target="_blank">Terms of Service</a>, <a href="/privacy/" target="_blank">Privacy Policy</a>, and <a href="/community-guidelines/" target="_blank">Community Guidelines</a>'
        }

class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    def login(self):
        user = authenticate(
            self.request,
            username=self.cleaned_data.get('username'),
            password=self.cleaned_data.get('password')
        )
        if user:
            login(self.request, user)
            return True
        return False
    
class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'title',
            'email',
            'city',
            'state',
            'country',
            'bio',
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }    
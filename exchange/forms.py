from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=True)
    username = forms.CharField(max_length=150, required=True)
    city = forms.CharField(max_length=255, required=False)
    state = forms.CharField(max_length=255, required=False)
    country = forms.CharField(max_length=255, required=False)
    zip_code = forms.CharField(max_length=20, required=False)
    terms_agreed = forms.BooleanField(required=True, label="I agree to the terms of service, privacy policy, and community guidelines")

    class Meta:
        model = User
        fields = ('email', 'full_name', 'username', 'password1', 'password2', 'city', 'state', 'country', 'zip_code', 'terms_agreed')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.full_name = self.cleaned_data['full_name']
        user.username = self.cleaned_data['username']
        user.city = self.cleaned_data['city']
        user.state = self.cleaned_data['state']
        user.country = self.cleaned_data['country']
        user.zip_code = self.cleaned_data['zip_code']
        user.terms_agreed = self.cleaned_data['terms_agreed']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
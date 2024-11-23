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
        fields = ['full_name', 'city', 'state', 'country', 'zip_code', 'terms_agreed']

        widgets = {
            'full_name': forms.TextInput(attrs={'required': True}),
            'terms_agreed': forms.CheckboxInput(attrs={'required': True}),
        }

        labels = {
            'terms_agreed': 'I agree to the <a href="/terms/" target="_blank">Terms of Service</a>, <a href="/privacy/" target="_blank">Privacy Policy</a>, and <a href="/community-guidelines/" target="_blank">Community Guidelines</a>'
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your username or email')
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': _('Enter your password')
        })
    )
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(), label=_("Remember me"))

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            self.user = self._get_user_by_username_or_email(username)
            if self.user is None:
                raise ValidationError(
                    _("Invalid username or email."),
                    code='invalid_login'
                )
            if not self.user.is_active:
                raise ValidationError(
                    _("This account is inactive."),
                    code='inactive_account'
                )
        return username

    def _get_user_by_username_or_email(self, username):
        try:
            user = User.objects.get(email__iexact=username)
            return user
        except User.DoesNotExist:
            try:
                user = User.objects.get(username__iexact=username)
                return user
            except User.DoesNotExist:
                return None

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and self.user:
            if not self.user.check_password(password):
                raise ValidationError(
                    _("Invalid password."),
                    code='invalid_login'
                )
        return password

    def clean(self):
        cleaned_data = super().clean()
        if self.user:
           # This method would be called if all fields are valid.
            user = authenticate(self.request, username=self.user.email, password=cleaned_data.get('password'))

            if user is None:
                 raise ValidationError(
                     _("Unable to log in with provided credentials."),
                     code='invalid_login'
                 )
            else:
                self.user_cache = user

        return cleaned_data

    def login(self):
        if self.is_valid():
            login(self.request, self.user_cache)
            if not self.cleaned_data.get('remember_me'):
               # Set session expiry to browser close if remember me is not checked.
                self.request.session.set_expiry(0)
            return True
        return False
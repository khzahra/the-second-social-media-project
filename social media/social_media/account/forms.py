from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label="نام کاربری", widget=forms.
                               TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید.'}))
    email = forms.EmailField(label="ایمیل", widget=forms.
                             EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید.'}))
    password1 = forms.CharField(label="رمز عبور", widget=forms.
                               PasswordInput(attrs={'class': 'form-control', 'placeholder': "رمز عبور خود را وارد کنید."}))
    password2 = forms.CharField(label="تایید رمز عبور", widget=forms.
                               PasswordInput(attrs={'class': 'form-control', 'placeholder': "رمز عبور خود را مجددا وارد کنید."}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('ایمیل تکراری است!')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError("نام کاربری قبلا ثبت شده است!")
        return username

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError("رمز عبور باید یکسان باشد!")


class UserLoginForm(forms.Form):
    username = forms.CharField(label="نام کاربری یا ایمیل", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری یا ایمیل خود را وارد کنید.'}))
    password = forms.CharField(label="رمز عبور", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder' : 'رمز عبور خود را وارد کنید'}))


class EditUserForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = Profile
        fields = ('age', 'bio')
        widget = {
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'},)
        }


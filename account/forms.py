from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import CustomUser




class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-custom',
                'placeholder': 'Mot de passe',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-custom',
                'placeholder': 'Confirmer le mot de passe',
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'Email'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control form-control-custom', 'placeholder': 'Nom complet'}),
        }
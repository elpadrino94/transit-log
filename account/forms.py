from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import CustomUser, Profile




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

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['phone_number', 'bio',]
        widgets = {
            
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+228 90 xx xx xx'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entrez votre bio', 'row': 4})
        }
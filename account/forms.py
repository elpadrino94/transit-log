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
    full_name = forms.CharField(max_length=150,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
                                )
    avatar = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    class Meta:
        model = Profile 
        fields = ['phone_number', 'bio']
        widgets = {
            
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+228 90 xx xx xx'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entrez votre bio', 'rows': 4})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].initial = self.instance.user.full_name


    def save(self, commit=True):
        profile = super().save(commit=False)

        # Modifier le nom complet de l'utilisateur associé au profil
        profile.user.full_name = self.cleaned_data['full_name']

        # Modifie la photo uniquement si un fichier a été téléchargé
        if self.cleaned_data.get('avatar'):
            profile.user.avatar = self.cleaned_data['avatar']

        if commit:
            profile.user.save()
            profile.save()
        return profile


class CustomUserUpdateForm(forms.ModelForm):
    full_name = forms.CharField(max_length=150,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
                                )
    
    phone_number = forms.CharField(max_length=20, 
                                   widget=forms.TextInput(attrs={
                                       'class':'form-control', 'placeholder': '+228 90 xx xx xx'
                                   }))
    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control', 'placeholder': 'Entrez votre bio', 'rows':4
        })
    )
    avatar = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = CustomUser
        fields = ['full_name', 'avatar']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pré-remplir les champs du profil si l'instance (User) a un profil associé
        if self.instance and hasattr(self.instance, 'profile'):
            self.fields['phone_number'].initial = self.instance.profile.phone_number
            self.fields['bio'].initial = self.instance.profile.bio

    def save(self, commit=True):
        # 1. Sauvegarde l'utilisateur (CustomUser) pour full_name et avatar
        user = super().save(commit=commit)

        if self.cleaned_data.get('avatar'):
            user.avatar = self.cleaned_data['avatar']
            if commit:
                user.save()
        
        if commit:
            # 2. Récupère ou crée le profil associé et sauvegarde phone_number et bio
            profile, created = Profile.objects.get_or_create(user=user)
            profile.phone_number = self.cleaned_data.get('phone_number')
            profile.bio = self.cleaned_data.get('bio')
            profile.save()
            
        return user

    

        

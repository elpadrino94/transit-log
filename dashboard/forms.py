from django import forms 

from app.models import Post, Category


ICON_CHOICES = [
    ("bi bi-truck", "Transport routier"),
    ("bi bi-water", "Transport maritime"),
    ("bi bi-airplane", "Transport aérien"),
    ("bi bi-file-earmark-check", "Transit douanier"),
    ("bi bi-box-seam", "Logistique"),
    ("bi bi-globe", "Import / Export"),
    ("bi bi-cart", "Commerce"),

    
]

class CategoryAddForm(forms.ModelForm):

    icon = forms.ChoiceField(
        choices=ICON_CHOICES,
        widget=forms.Select(attrs={
            "class": "form-select",
        })
    )
    class Meta:
        model = Category
        fields = ['name', 'description', 'meta_title', 'meta_description', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'category-name', 'placeholder': 'Entrez le nom de la catégorie'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'category-description', 'placeholder': 'Rédiger une description pour la catégorie', 'rows': 3}),
            'meta_title': forms.TextInput(attrs={'class': 'form-control', 'id': 'meta-title', 'placeholder': 'Titre SEO optimisé'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'id': 'meta-description', 'placeholder': 'Description SEO optimisée', 'rows': 3}),

        }



class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'image', 'status', 'category', 'meta_title', 'meta_description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le titre de votre article'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Rédiger un résume', 'rows':3}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Rédigez le contenu complet de votre article...', 'rows': 5}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'meta_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre SEO optimisé'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description SEO optimisée', 'rows': 3}),
        }


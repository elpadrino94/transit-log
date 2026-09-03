from django import forms 

from app.models import Post, Category


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'meta_title', 'meta_description']
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


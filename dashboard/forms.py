from django import forms 

from app.models import Post, Category


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'meta_title', 'meta_description']



class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'image', 'status', 'category', 'meta_title', 'meta_description']


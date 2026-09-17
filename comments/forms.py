from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'id': 'comment-message', 'class': 'form-control', 'placeholder': 'Write your comment here...'}),
        }


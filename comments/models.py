from django.db import models

from app.models import Post
from config.settings import AUTH_USER_MODEL

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title[:20] + '...' + ' - ' + self.user.full_name
    

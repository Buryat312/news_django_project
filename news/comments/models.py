from django.db import models
from django.utils.translation import activate
from posts.models import Post
# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL,
                            null=True, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField() #поле
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
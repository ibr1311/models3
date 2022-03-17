from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Comment(models.Model):
    text = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)

class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

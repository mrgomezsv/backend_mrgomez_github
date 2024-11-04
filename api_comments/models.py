# models.py
from django.db import models

class Comment(models.Model):
    user_id = models.IntegerField()
    full_name = models.CharField(max_length=255)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}: {self.comment_text[:20]}"

# serializers.py
from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user_id', 'full_name', 'comment_text', 'created_at']

from rest_framework import serializers
from ..models import ForumPost, Comment

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'created_at', 'updated_at', 'author']
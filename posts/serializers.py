from rest_framework import serializers


from posts.models import Post, Comment, LikePost, LikeComment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'body', 'slug', 'photo', 'location', 'likes',
                  'created_at', 'updated_time', 'is_enabled']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'reply', 'text', 'created_at']


class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = ['post', 'user', 'created_at']


class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComment
        fields = ['comment', 'user', 'created_at']
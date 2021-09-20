from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from posts.serializers import CommentSerializer, PostSerializer, LikeCommentSerializer, LikePostSerializer
from posts.models import Comment, Post
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView


class CommentListApiView(ListCreateAPIView):
    query_set = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return Comment.objects.all()


class PostListApiView(ListCreateAPIView):
    query_set = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        Post.objects.create(user=self.request.user, **serializer.validated_data)



class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikePostListCreateAPIView(APIView):

    def get(self, request, pk):
        post = Post.objects.filter(pk=pk)
        like_count = post.likepost.count()
        serializer = LikePostSerializer(like_count, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        user = request.user
        post = Post.objects.filter(pk=pk)
        serializer = LikePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeCommentListCreateAPIView(APIView):

    def get(self, request, pk):
        comment = Comment.objects.filter(pk=pk)
        like_count = comment.likepost.count()
        serializer = LikeCommentSerializer(like_count, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        user = request.user
        comment = Comment.objects.filter(pk=pk)
        serializer = LikeCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(comment, user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
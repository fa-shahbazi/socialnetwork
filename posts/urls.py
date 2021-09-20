from django.urls import path
from . import views
app_name = 'posts'
urlpatterns = [
    path('postlist/', views.PostListApiView.as_view(), name='post_list'),
    path('<int:pk>/likecomment/', views.LikeCommentListCreateAPIView.as_view(), name='like_comment'),
    path('<int:pk>/likepost/', views.LikePostListCreateAPIView.as_view(), name='like_post'),
    path('commentlist/', views.CommentListApiView.as_view(), name='comment_list'),

]
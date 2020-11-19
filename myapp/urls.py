from myapp import views
from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView
)


urlpatterns= [
    path('', PostListView.as_view(), name='blog-home'),
    path('postsofuser/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('postdetail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('postcreate/new/', PostCreateView.as_view(), name='post-create'),
    path('postdetail/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('postdetail/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete')
]

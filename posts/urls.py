from django.urls import path

from .views import PostUpdateView, PostCreateView, PostDetailView, PostListView

urlpatterns = [
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='posts-update'),
    path('new/', PostCreateView.as_view(), name='posts-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='posts-detail'),
    path('', PostListView.as_view(), name='posts-list'),
]
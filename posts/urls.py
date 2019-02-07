from django.urls import path

from .views import PostUpdateView, PostCreateView, PostDetailView, PostListView


app_name = 'posts'

urlpatterns = [
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('new/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('', PostListView.as_view(), name='list'),
]
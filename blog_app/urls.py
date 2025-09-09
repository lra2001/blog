from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), #Changed here
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'), #Url pattern here
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # Added the url pattern
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # Added in new url pattern
    path('about/',views.about, name='blog-about'),
]
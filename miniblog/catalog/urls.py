from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('blog/<int:pk>/update', views.index, name='blog-update'),
    path('blog/<int:pk>/delete', views.index, name='blog-delete'),
    path('author/<int:pk>/update', views.index, name='author-update'),
    path('author/<int:pk>/delete', views.index, name='author-delete'),
    path('blog/<int:pk>/comment/', views.CommentCreate.as_view(), name = 'comment-create')
]

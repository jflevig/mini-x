from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('crear/', views.PostCreateView.as_view(), name='crear_post'),
    path('editar/<int:pk>/', views.PostUpdateView.as_view(), name='editar_post'),
    path('eliminar/<int:pk>/', views.PostDeleteView.as_view(), name='eliminar_post'),
    path('detalle/<int:pk>/', views.PostDetailView.as_view(), name='detalle_post'),
    path('post_like/<int:post_id>', views.like_post, name='like_post'),
]
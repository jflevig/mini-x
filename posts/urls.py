from django.urls import path
from . import views

urlpatterns = [
    # Rutas para la gestión de posts
    path('', views.PostListView.as_view(), name='home'),
    path('crear/', views.PostCreateView.as_view(), name='crear_post'),
    path('editar/<int:pk>/', views.PostUpdateView.as_view(), name='editar_post'),
    path('eliminar/<int:pk>/', views.PostDeleteView.as_view(), name='eliminar_post'),
    path('detalle/<int:pk>/', views.PostDetailView.as_view(), name='detalle_post'),
    
    # Rutas para la gestión likes (dependiendo de la vista desde la que se da like)
    path('post_like_home/<int:post_id>', views.like_post_home, name='like_post_home'),
    path('post_like_detalle/<int:post_id>', views.like_post_detalle, name='like_post_detalle'),
    path('post_like_perfil/<int:post_id>', views.like_post_perfil, name='like_post_perfil'),
]
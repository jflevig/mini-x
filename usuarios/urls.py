from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registro/', registro, name='registro'),
    path('perfil/<int:pk>/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
]
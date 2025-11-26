from django.shortcuts import render, redirect
from django.views.generic import ListView ,CreateView, UpdateView, DeleteView, DetailView
from .models import Post, Comentario
from .forms import PostForm, ComentarioForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


class PostListView(ListView):
    model = Post
    template_name = 'posts_lista.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts_crear.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts_editar.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.usuario
    
    def handle_no_permission(self): #403: Forbidden
        #redirect pagina sin permisos
        return redirect('pagina_sinpermisos')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts_eliminar.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.usuario
    
    def handle_no_permission(self): #403: Forbidden
        #redirect pagina sin permisos
        return redirect('pagina_sinpermisos')

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts_detalle.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = Comentario.objects.filter(post=self.object).order_by('-created_at')
        context['form'] = ComentarioForm()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.post = self.object
            comentario.save()
            return redirect('detalle_post', pk=self.object.pk)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


@login_required
def like_post_home(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('home')

@login_required
def like_post_detalle(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect(reverse_lazy('detalle_post', kwargs={'pk': post.id}))

@login_required
def like_post_perfil(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect(reverse_lazy('perfil', kwargs={'pk': post.usuario.pk}))
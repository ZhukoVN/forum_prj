from django.shortcuts import render, redirect
from service.models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, CommentForm, UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

def index(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

class RegisterForm(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    success_message = "%(username)s was created successfully"
    template_name = 'register.html'
    success_url = reverse_lazy('login')



class PostsView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-created_at']

class DetailPostsView(DetailView):
    model = Post
    template_name = 'detail_post.html'

#class CreatePostView(PermissionRequiredMixin, CreateView):
#    permission_required = 'service.add_post'
#    model = Post
#    template_name = 'create_post.html'
#    form_class = PostForm

@login_required
@permission_required('service.add_post')
def create_post(req):
    form = PostForm()
    if req.method == 'POST':
        form = PostForm(req.POST)
        if form.is_valid():            
            form.save()
            title = form.cleaned_data.get('title')
            #if title != 'POST':
            #    messages.error(req, f'Something went wrong')
            #    return redirect('index')
            #id = form.cleaned_data.get('id')
            messages.success(req, f'Post {title} was created successfully')
            return redirect('index')
        
    return render(req, 'create_post.html', {'form': form})

class UpdatePostView(PermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_post'
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm

class DeletePostView(PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete_post'
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
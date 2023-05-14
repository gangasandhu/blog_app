from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .models import Post, Comment
from .forms import CommentForm, CreatePostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView, UpdateView
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-date_posted')
    posts_per_page = 3
    paginator = Paginator(posts, posts_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, 'blog/index.html', context)

def post(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    posts = Post.objects.order_by('-date_posted')[:9]

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(reverse('blog-post', kwargs={'id': id}) + '#comment-section')
    else:
        form = CommentForm()
    return render(request, 'blog/post.html', { "post": post, 'comments': comments, 'form':  form, 'posts': posts})

def sample(request):
    return render(request, 'blog/sample.html')

@login_required(login_url='/login/')
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = CreatePostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = '/'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
        

class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'blog/edit_post.html'
    success_url = reverse_lazy('blog-home')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

def about(request):
    return render(request, 'blog/about.html')
from django.shortcuts import render
from .models import Author, Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    num_posts = Post.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_posts': num_posts},
    )

def base(request):
    num_posts = Post.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'base.html',
        context={'num_posts': num_posts, 'num_visits': num_visits},
    )

class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    paginate_by = 1

    def get_queryset(self):
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

class PostDetailView(generic.DetailView):
    model = Post

class AuthorListView(generic.ListView):
    model = Author
    queryset = Author.objects.all()

    def get_queryset(self):
        return self.queryset

class AuthorDetailView(generic.DetailView):
    model = Author

class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title', 'body']




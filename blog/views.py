# from Django.shortcuts import render gør at vi kan returnere en rendered template i stedet for HTTPresponse 
from django.shortcuts import render 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


def home(request):
    context = {
        # Jeg laver en query for at vise alle posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
    

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-Dato']

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['Titel', 'Content']

    def form_valid(self, form):
        # Den form du prøver at submit, før du gør det tag den instance og sæt Forfatteren = den aktuelle User som er logget ind. 
        form.instance.Forfatter = self.request.user
        # Den her linje køre bare form valid metoden på vores parent klasse. 
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['Titel', 'Content']

    def form_valid(self, form):
        # Den form du prøver at submit, før du gør det tag den instance og sæt Forfatteren = den aktuelle User som er logget ind. 
        form.instance.Forfatter = self.request.user
        # Den her linje køre bare form valid metoden på vores parent klasse. 
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Forfatter:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Forfatter:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
    
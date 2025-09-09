from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# posts = [
#     {
#         'author': 'Steve K',
#         'title': 'First Blog Post',
#         'content': 'Content for the first post.',
#         'date_posted': '12/07/2023'
#     },

#      {
#         'author': 'Scott K',
#         'title': 'Second Blog Post',
#         'content': 'Content for the second post.',
#         'date_posted': '13/07/2023'
#     }

# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html Changed here.
    context_object_name = 'posts' #Updated here. Now the default name is set equal to 'posts'
    ordering = ['-date_posted'] #Change here the - will order the posts from newest to oldest.

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    #Overriding form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user # Set the author on the form
        return super().form_valid(form) # Validate form by running form_valid method from parent class.

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # New class created and UpdateView passed in.
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #Added a new function here to check the user author is correct for the spefice Post.
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # New class PostDeleteView created here
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = "/" # Here we are redirecting the user back to the homepage after deleting a Post successfully

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
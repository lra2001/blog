from django.shortcuts import render
from django.http import HttpResponse
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

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
from django.shortcuts import render
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:5] # the projects on the page will be showing us the most current one no the top
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

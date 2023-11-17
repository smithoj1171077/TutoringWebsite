from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

# gets the blog and related blogs for viewing when a blog is clicked on
def blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    related_blogs = Blog.objects.filter(subject=blog.subject).exclude(pk=pk)[0:3]
    return render(request, 'blog/fullblog.html', {
        'blog': blog,
        'related_blogs': related_blogs
    })

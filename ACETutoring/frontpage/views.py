from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog, Subject

# Create your views here.

# this view renders the front page 
def frontpage(request):
    return render(request,'frontpage/frontpage.html')

def index_blogs(request):
    blogs = Blog.objects.filter()[0:6]

    return render(request,'frontpage/blogindex.html',{
        'blogs' : blogs
    })



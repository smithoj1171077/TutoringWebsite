from django.shortcuts import render

# Create your views here.

# this view renders the front page 
def frontpage(request):
    return render(request,'frontpage/frontpage.html')



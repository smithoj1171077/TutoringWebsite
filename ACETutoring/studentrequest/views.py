from django.shortcuts import render, redirect
from .forms import StudentRequestForm, YearLevel
# Create your views here.

def new(request):
    if request.method == 'POST':
        form = StudentRequestForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()

            return redirect('frontpage:blog')
    else:
        form = StudentRequestForm()

    return render(request,'studentrequest/requestform.html', {
        'form': form,
        'title': 'New student request form',
    })

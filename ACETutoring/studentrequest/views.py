from django.shortcuts import render, redirect
from .forms import StudentRequestForm, YearLevel
# Create your views here.

def new(request):
    if request.method == 'POST':
        form = StudentRequestForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            # if success, return to home 
            return redirect('frontpage:blogindex')
        else:
            # if form invalid display form with errors
            return render(request,'studentrequest/requestform.html', {
                'form': form,
                 'title': 'New student request form',
                   })
    else:
        # if form needs to be generated, instantiate a blank form 
        form = StudentRequestForm()
    return render(request,'studentrequest/requestform.html', {
                'form': form,
                 'title': 'New student request form',
                   })
    

from django import forms

from .models import RevisionBook

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

# the form for the creating new revision books for sale
class NewRevisionBookForm(forms.ModelForm):
    class Meta:
        model = RevisionBook
        fields = ('subject', 'title','price','image','description')
        widgets = {
            'subject': forms.Select(attrs = {
            'class': INPUT_CLASSES
            }),
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            })

    }
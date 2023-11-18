from django import forms
from .models import StudentRequest, Subject, YearLevel

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border bg-gray-100'


"""This class has the fields and input formats for the form customers fill out to request tutoring services"""
class StudentRequestForm(forms.ModelForm):
    class Meta:
        model = StudentRequest 
        fields = (
            'subject 1','subject 2 (optional)','subject 3 (optional)','subject 4 (optional)','student name','are you parent/guardian','parent/guardian name','students email',
            'parent/guardian email','phone number', 'year level', 
            'online only'
            )
        # the customer may select multiple subjects to request 
        widgets = {
            'subject 1' : forms.Select(attrs={
                'classes' : INPUT_CLASSES
            }),
            'subject 2 (optional)' : forms.Select(attrs={
                'classes' : INPUT_CLASSES
            }),
            'subject 3 (optional)' : forms.Select(attrs={
                'classes' : INPUT_CLASSES
            }),
            'subject 4 (optional)' : forms.Select(attrs={
                'classes' : INPUT_CLASSES
            }),
            'student name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'are you parent/guardian': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
            'parent/guardian name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'students email': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'parent/guardian email': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'phone number' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }), 
            'year level': forms.Select(attrs={
                'class': INPUT_CLASSES
            }), 
            'online only': forms.Select(attrs={
                'class': INPUT_CLASSES
            }), 
        }
        


from django import forms
from .models import StudentRequest, Subject, YearLevel
from .postcodeValidatorFacade import PostCodeValidatorInterface
from django.core.exceptions import ValidationError



INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border bg-gray-100'


"""This class has the fields and input formats for the form customers fill out to request tutoring services"""
class StudentRequestForm(forms.ModelForm):
    class Meta:
        model = StudentRequest 
        fields = (
            'subject1','subject2_optional','subject3_optional','subject4_optional','student_name','are_you_parent_or_guardian','parent_or_guardian_name','students_email',
            'parent_or_guardian_email','phone_number', 'year_level', 
            'online_only','postcode'
            )
        # the customer may select multiple subjects to request 
        widgets = {
            'subject1' : forms.Select(attrs={
                'class' : INPUT_CLASSES
            }),
            'subject2_optional' : forms.Select(attrs={
                'class' : INPUT_CLASSES
            }),
            'subject3_optional' : forms.Select(attrs={
                'class' : INPUT_CLASSES
            }),
            'subject4_optional' : forms.Select(attrs={
                'class' : INPUT_CLASSES
            }),
            'student_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'are_you_parent_guardian': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }),
            'parent_guardian_or_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'students_email': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'parent_guardian_email': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'phone_number' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }), 
            'year_level': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'postcode': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'online_only': forms.CheckboxInput(attrs={
                'class': INPUT_CLASSES
            }), 
        }
        
    # helper function to make code concise 
    def at_least_n(self,n, fields):
        if sum(list(map(lambda x: 1 if x != None else 0,fields))) >= n:
            return True
        return False

    # raises error if no subject is entered in any field     
    def clean_no_filled_subjects(self,subjects):
         if self.at_least_n(n=1, fields = subjects) == False:
            raise ValidationError(
                'need to enter at least one subject'
                )
         
    # raises error if the post code is too far or not found
    def clean_post_code(self,postcode,onlineOnly):
         pc_validity = PostCodeValidatorInterface.validate(postcode)
    
         if (pc_validity == False) and not onlineOnly:
              raise ValidationError(
                'postcode too far'
            )
               
         elif (pc_validity == "Postcode not found"):
              raise ValidationError(
                'no matching Australian post code found'
            )
         
    # makes sure at least one piece of contact info is provided
    def clean_contact_info(self,student_email,parent_email,phone):
         if not self.at_least_n(n=1,fields=(student_email,parent_email,phone)):
            for field in (student_email,parent_email,phone):
                raise ValidationError(
                    'at least one of student email, parent/guradian email, or phone number required'
                )
            
    # makes sure that there is not a year level subject mismatch
    def clean_year_level_subject_mismatch(self,year_level,subjects):
        for i in range(0, len(subjects)):
            if subjects[i] != None:
                subject_year_level_match = False
                for valid_year_level in subjects[i].year_level.all():
                    if(str(year_level) == str(valid_year_level)):
                        subject_year_level_match = True
                if subject_year_level_match == False:
                            raise ValidationError(
                                'We do not provide tutoring services to this level of this subject unfortunately'
                                )
         
         
         
    def clean(self):
        cleaned_data = super().clean()
        #----------------at least one subject-------------------------
        subject1 = cleaned_data.get('subject1') 
        subject2 = cleaned_data.get('subject2_optional')
        subject3 = cleaned_data.get('subject3_optional')
        subject4 = cleaned_data.get('subject4_optional')
        subjects = (subject1, subject2, subject3, subject4)
            
        self.clean_no_filled_subjects(subjects)
              
        #---------------post code validation-----------------------------------
        postcode = cleaned_data.get('postcode')
        onlineOnly = cleaned_data.get('online_only')
        self.clean_post_code(postcode, onlineOnly)
        
               
        #-----------------------contact info validation-------------------------------
        student_email = cleaned_data.get('students_email')
        parent_email = cleaned_data.get('parent_or_guardian_email')
        phone = cleaned_data.get('phone_number')
        self.clean_contact_info(student_email, parent_email,phone)
        
                    
        #------------------------year level -> subject mapping validation-------------------------------------
        year_level = cleaned_data.get('year_level')
        self.clean_year_level_subject_mismatch(year_level, subjects)
        
        return cleaned_data
            





            

        


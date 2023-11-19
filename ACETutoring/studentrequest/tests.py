from django.test import TestCase
from .forms import StudentRequestForm
import copy
from django.core.exceptions import ValidationError

class TestStudentRequestForm(TestCase):
    form_data = {
        'subject1' : 'English',
        'subject2_optional': None,
        'subject3_optional': None,
        'subject4_optional': None,
        'student_name' : 'James Smith',
        'are_you_parent_or_guardian' : False,
        'parent_or_guardian_name' : 'Matt Smith',
        'students_email' : 'JamesSmith@email.com',
        'parent_or_guardian email': 'MattySmith@email.com',
        'phone_number' : '0438498430', 
        'year_level' : 'VCE 1/2', 
        'online_only': True,
        'postcode' : '3102'
    }
    
    # to avoid repeative code this modifies the original form to suit each test case
    def get_changed_form(self, changes_dict):
        print(self.form_data)
        test_form_data = copy.copy(self.form_data)
        for key, value in changes_dict.items():
            test_form_data[key] = value
        return StudentRequestForm(data=test_form_data)
    
    
    # check if not requesting more than 1 subject is allowed
    def test_accept_valid_form(self):
        test_form_data = self.form_data
        form = StudentRequestForm(data=test_form_data)
        try: 
            if form.is_valid():
                form.clean()
        except ValidationError as e:
            print(f"Validation Error Message: {e}")


        with self.assertFalse(self.assertRaises(ValidationError)) as context:
            if form.is_valid():
                form.clean()
    
    # check if no subjects is invalid
    def test_no_subjects(self):
        print(self.get_changed_form({'subject1': None}).is_valid())
        form = self.get_changed_form({'subject1': None})
        with self.assertRaises(ValidationError) as context:
            form.clean()
    
    #------------------- check if it handles postcodes correctly -------------------------
    
    #----------------------online only false case-----------------------------------
    # check if the not found message is returned for a string which can not be an australian postcode 
    def test_invalid_postcode(self):
        self.assertFalse(self.get_changed_form({'postcode':"1122932949",'online_only': False}).is_valid())
    
    
    
    # check if false is returned for a geelong postcode 
    def test_far_postcode(self):
        self.assertFalse(self.get_changed_form({'postcode':"3220",'online_only': False}).is_valid())
        
    # check if true is returned for a postcode in the service area 
    def test_close_postcode(self):
        self.assertTrue(self.get_changed_form({'postcode':"3121", 'online_only': False}).is_valid())

    # -------------------------------online only true case ------------------------------------

    # check if the not found message is returned for a string which can not be an australian postcode 
    def test_invalid_postcode(self):
        self.assertTrue(self.get_changed_form({'postcode':"1122932949",'online_only': True}).is_valid())
    
    # check if false is returned for a geelong postcode 
    def test_far_postcode(self):
        self.assertTrue(self.get_changed_form({'postcode':"3220",'online_only': True}).is_valid())
        
    # check if true is returned for a postcode in the service area 
    def test_close_postcode(self):
        self.assertTrue(self.get_changed_form({'postcode':"3121", 'online_only': True}).is_valid())

    #-----------------------contact information------------------------------------------------------

    """We need to test that the business rule: at least one of: student email, parent email or phone number is implemented correctly
    so the form is valid if only one of those fields are filled"""
    
    # check if it accepts when there is only a phone number 
    def test_phone_only(self):
        self.assertTrue(self.get_changed_form({'students_email': None, 'parent_or_guardian email': None}).is_valid())

    # check if it accepts when there is only a student email
    def test_student_email_only(self):
        self.assertTrue(self.get_changed_form({'phone_number': None, 'parent_or_guardian email': None}).is_valid())
    
    # check if it accepts when there is only a parent/guardian email
    def test_phone_only(self):
        self.assertTrue(self.get_changed_form({'phone_number': None, 'students_email': None}).is_valid())
    
    # check if it rejects if there is no contact info
    def test_no_contact_info(self):
        self.assertFalse(self.get_changed_form({'phone_number': None, 'students_email': None, 'parent_or_guardian_email': None}).is_valid())
   
    #---------------------------------------year level-------------------------------------------------------
    """Business rule: customers can not submit a request for tutition in a subject outside of their year level,
    the business owner can chose what year levels they will offer each subject to"""

    # check if a year 9 is not allowed to take maths methods
    def too_young_for_subject(self):
        self.assertFalse(self.get_changed_form({'year_level':"9",'subject1': "Mathematical Methods"}).is_valid())

    # test if a year 10 is allowed to be tutored for english
    def right_age(self):
        self.assertTrue(self.get_changed_form({'year_level':"10",'subject1': "English"}).is_valid())

    # check if a year 9 is not allowed to take maths methods if input in the subject 2 box
    def too_young_for_subject_2(self):
        self.assertFalse(self.get_changed_form({'year_level':"9",'subject2': "Mathematical Methods"}).is_valid())

    # test if a year 10 is allowed to be tutored for english if put in the subject 2 box 
    def right_age_subject_2(self):
        self.assertTrue(self.get_changed_form({'year_level':"10",'subject2': "English"}).is_valid())


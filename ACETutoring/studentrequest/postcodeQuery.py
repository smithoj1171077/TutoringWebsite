from .exceptions import PostcodeNotFoundException

"""This class has functions which handle if a post code is possible to offer in person 
tutoring for, it is done by a distance threshold between the there the tutoring business
is centrally located and the reported postcode in the form"""
class PostCodeValidation:
    #-------------static variables------------------------------------
    # distances are measured from this post code
    home_postcode = "3103"
    # the limiting distance in kms
    cutoff_distance = 30 


    def __init__(self, distance_query_interface):
        # set the adapter to distance calculation library
        self.distance_query_interface = distance_query_interface

    # determine if tutor session can be held at student's home 
    def postcode_in_service_area(self, student_postcode):
            try:
                 distance = self.distance_query_interface.check_distance(PostCodeValidation.home_postcode, student_postcode)
            except PostcodeNotFoundException: 
                 return "Postcode not found"
            else:
                if distance <= PostCodeValidation.cutoff_distance:
                      return True
                elif distance > PostCodeValidation.cutoff_distance:
                      return False
              

        
"""this is the interface postcode validation is exposed to, it has the same check_distance method regardless of the library used to compute
the distance """
class DistanceQueryInterface:
    def check_distance(self, home_postcode,student_postcode):
        pass






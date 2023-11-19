from .pgeocodeAdapter import PGeoCodeAdapter
from .postcodeQuery import PostCodeValidation

class PostCodeValidatorInterface:
    adapter = PGeoCodeAdapter()
    validator = PostCodeValidation(adapter)
    
    def validate(student_postcode):
        return PostCodeValidatorInterface.validator.postcode_in_service_area(student_postcode)
        
    
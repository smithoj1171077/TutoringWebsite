from .postcodeQuery import DistanceQueryInterface
import pgeocode
import numpy as np 
from .exceptions import PostcodeNotFoundException

"""The adapter class protects the system from variation in the
library used to retrieve the coordinates"""
class PGeoCodeAdapter(DistanceQueryInterface):
    def check_distance(self, home_post_code, student_post_code):
        # set the calculator to australian postcodes and throw an exception if postcode not found
        distance_calculator = pgeocode.GeoDistance(country='AU',errors='error')
        validity_query = pgeocode.Nominatim(country='AU')
    
        # returns pandas df, if there is not an associated lattitude then it is not considered a valid postcode 
        validity_query.query_postal_code(int(student_post_code))['latitude']
        if(np.isnan(validity_query.query_postal_code(int(student_post_code))['latitude'])):
            raise PostcodeNotFoundException
        
        return distance_calculator.query_postal_code(int(home_post_code),int(student_post_code))
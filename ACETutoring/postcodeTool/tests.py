# test if an invalid post code is given
import unittest
from postcodeQuery import PostCodeValidation
from pgeocodeAdapter import PGeoCodeAdapter

class TestPGeoCodeAdaptor(unittest.TestCase):
    adaptor = PGeoCodeAdapter()
    validator = PostCodeValidation(adaptor)

    # check if the not found message is returned for a string which can not be an australian postcode 
    def test_invalid_postcode(self):
        self.assertEqual("Postcode not found", self.validator.postcode_in_service_area("11232342"))
    
    # check if false is returned for a geelong postcode 
    def test_far_postcode(self):
        self.assertEqual(False, self.validator.postcode_in_service_area("3220"))
        

    def test_close_postcode(self):
        self.assertEqual(True, self.validator.postcode_in_service_area("3121"))

    

if __name__ == '__main__':
    unittest.main()
        
    
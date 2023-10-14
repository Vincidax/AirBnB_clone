import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test the functionality of the Amenity class
    """

    def setUp(self):
        """
        Set up the tests
        """
        self.amenity = Amenity()

    def test_init(self):
        """
        Test the __init__ method
        """
        self.assertIsInstance(self.amenity, Amenity)
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        """
        Test if Amenity class inherits from BaseModel
        """
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """
        Test if Amenity class contains name attribute
        """
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_attribute_types(self):
        """
        Test the type of Amenity class attributes
        """
        self.assertIsInstance(self.amenity.name, str)


if __name__ == '__main__':
    unittest.main()

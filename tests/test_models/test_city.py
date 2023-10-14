import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Test the functionality of the City class"""

    def setUp(self):
        """Set up the tests"""
        self.city = City()

    def test_init(self):
        """Test the __init__ method"""
        self.assertIsInstance(self.city, City)
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_inheritance(self):
        """Test if City class inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test if City class contains state_id and name attributes"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_attribute_types(self):
        """Test the type of City class attributes"""
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

if __name__ == '__main__':
    unittest.main()

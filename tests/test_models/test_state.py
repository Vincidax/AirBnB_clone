import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """Test the functionality of the State class"""

    def setUp(self):
        """Set up the tests"""
        self.state = State()

    def test_init(self):
        """Test the __init__ method"""
        self.assertIsInstance(self.state, State)
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        """Test if State class inherits from BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Test if State class contains name attribute"""
        self.assertTrue(hasattr(self.state, "name"))

    def test_attribute_types(self):
        """Test the type of State class attributes"""
        self.assertIsInstance(self.state.name, str)

if __name__ == '__main__':
    unittest.main()

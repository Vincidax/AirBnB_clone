import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.file_storage = FileStorage()
        self.base_model = BaseModel()

    def tearDown(self):
        """Tear down for the tests"""
        del self.file_storage
        del self.base_model
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test the all method"""
        self.assertIsInstance(self.file_storage.all(), dict)

    def test_new(self):
        """Test the new method"""
        self.file_storage.new(self.base_model)
        key = "{}.{}".format(
            type(self.base_model).__name__,
            self.base_model.id
        )
        self.assertIn(key, self.file_storage.all())

    def test_save(self):
        """Test the save method"""
        self.file_storage.new(self.base_model)
        self.file_storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test the reload method"""
        self.file_storage.new(self.base_model)
        self.file_storage.save()
        key = "{}.{}".format(
            type(self.base_model).__name__,
            self.base_model.id
        )
        self.file_storage.reload()
        self.assertIn(key, self.file_storage.all())

    def test_new_none(self):
        """Test the new method with None"""
        with self.assertRaises(AttributeError):
            self.file_storage.new(None)

    def test_reload_no_file(self):
        """Test the reload method with no file"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.file_storage.reload()  # Should not raise


if __name__ == '__main__':
    unittest.main()

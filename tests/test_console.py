import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """
    Test cases for the HBNBCommand class.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.hbnb_cmd = HBNBCommand()

    def test_show_with_missing_class_name(self):
        """
        Test the 'show' command with a missing class name.
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_show("")
            self.assertTrue(mock_print.called)

    def test_show_with_invalid_class(self):
        """
        Test the 'show' command with an invalid class.
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_show("InvalidClass 123")
            self.assertTrue(mock_print.called)

    def test_show_with_missing_instance_id(self):
        """
        Test the 'show' command with a missing instance ID.
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_show("BaseModel")
            self.assertTrue(mock_print.called)

    def test_show_with_nonexistent_instance(self):
        """
        Test the 'show' command with a nonexistent instance.
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_show("BaseModel 123")
            self.assertTrue(mock_print.called)

    def test_destroy_with_missing_class_name(self):
        """
        Test the 'destroy' command with a missing class name.
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_destroy("")
            self.assertTrue(mock_print.called)

    def test_destroy_with_invalid_class(self):
        """
        Test the 'destroy' command with an invalid class.
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_destroy("InvalidClass 123")
            self.assertTrue(mock_print.called)

    def test_destroy_with_missing_instance_id(self):
        """
        Test the 'destroy' command with a missing instance ID.
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_destroy("BaseModel")
            self.assertTrue(mock_print.called)

    def test_destroy_with_nonexistent_instance(self):
        """
        Test the 'destroy' command with a nonexistent instance.
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_destroy("BaseModel 123")
            self.assertTrue(mock_print.called)

    def test_all_with_nonexistent_class(self):
        """
        Test the 'all' command with a nonexistent class.
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_all("InvalidClass")
            self.assertTrue(mock_print.called)

    def test_update_with_missing_class_name(self):
        """
        Test the 'update' command with a missing class name.
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_update("")
            self.assertTrue(mock_print.called)

    def test_update_with_invalid_class(self):
        """
        Test the 'update' command with an invalid class.
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_update("InvalidClass 123")
            self.assertTrue(mock_print.called)

    def test_update_with_missing_instance_id(self):
        """
        Test the 'update' command with a missing instance ID.
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_update("BaseModel")
            self.assertTrue(mock_print.called)

    def test_update_with_nonexistent_instance(self):
        """
        Test the 'update' command with a nonexistent instance.
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_update("BaseModel 123 attribute value")
            self.assertTrue(mock_print.called)


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Test cases for the HBNBCommand class
    """

    def setUp(self):
        """
        Setup for the test cases
        """
        self.hbnb_cmd = HBNBCommand()

    def test_show_with_missing_class_name(self):
        """
        Test case for show command with missing class name
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_show("")
            self.assertTrue(mock_print.called)

    def test_show_with_invalid_class(self):
        """
        Test case for show command with invalid class
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_show("InvalidClass 123")
            self.assertTrue(mock_print.called)

    def test_show_with_missing_instance_id(self):
        """
        Test case for show command with missing instance id
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_show("BaseModel")
            self.assertTrue(mock_print.called)

    def test_show_with_nonexistent_instance(self):
        """
        Test case for show command with nonexistent instance
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_show("BaseModel 123")
            self.assertTrue(mock_print.called)

    def test_destroy_with_missing_class_name(self):
        """
        Test case for destroy command with missing class name
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_destroy("")
            self.assertTrue(mock_print.called)

    def test_destroy_with_invalid_class(self):
        """
        Test case for destroy command with invalid class
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_destroy("InvalidClass 123")
            self.assertTrue(mock_print.called)

    def test_destroy_with_missing_instance_id(self):
        """
        Test case for destroy command with missing instance id
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_destroy("BaseModel")
            self.assertTrue(mock_print.called)

    def test_destroy_with_nonexistent_instance(self):
        """
        Test case for destroy command with nonexistent instance
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_destroy("BaseModel 123")
            self.assertTrue(mock_print.called)

    def test_all_with_nonexistent_class(self):
        """
        Test case for all command with nonexistent class
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_all("InvalidClass")
            self.assertTrue(mock_print.called)

    def test_update_with_missing_class_name(self):
        """
        Test case for update command with missing class name
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_update("")
            self.assertTrue(mock_print.called)

    def test_update_with_invalid_class(self):
        """
        Test case for update command with invalid class
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_update("InvalidClass 123")
            self.assertTrue(mock_print.called)

    def test_update_with_missing_instance_id(self):
        """
        Test case for update command with missing instance id
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_update("BaseModel")
            self.assertTrue(mock_print.called)

    def test_update_with_nonexistent_instance(self):
        """
        Test case for update command with nonexistent instance
        """
        with patch('builtins.print') as mock_print:
            self.hbnb_cmd.do_update("BaseModel 123 attribute value")
            self.assertTrue(mock_print.called)


if __name__ == '__main__':
    unittest.main()

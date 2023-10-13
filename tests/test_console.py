#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help show")
            output = f.getvalue().strip()
            self.assertIn("Prints the string representation of an instance", output)

    def test_count(self):
        # Implement test for count() functionality
        pass

    def test_show(self):
        # Implement test for show() functionality
        pass

    def test_destroy(self):
        # Implement test for destroy() functionality
        pass

    def test_update(self):
        # Implement test for update() functionality
        pass

if __name__ == '__main__':
    unittest.main()

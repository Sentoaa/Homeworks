import json
import unittest
from unittest.mock import patch
from io import StringIO
from Phonebook import *

with open('Phonebook.json', "w") as file:
    txt = {
    "phonebook": [
        {
            "telephone number": "22",
            "name": "3",
            "last name": "3",
            "full name": "3 3",
            "city": "3"
        }
    ]
}
    json.dump(txt, file)

class PhonbookTestCase(unittest.TestCase):

    def test_a_update_entry(self):
        test_data = '22\n1\n1\n1'
        expected_output = {
            "telephone number": "22",
            "name": "1",
            "last name": "1",
            "full name": "1 1",
            "city": "1"
        }
        with patch('sys.stdin', StringIO(test_data)):
            result = update_entry()
            with open('Phonebook.json', 'r') as file:
                result = json.load(file)
                for k, v in result.items():
                    self.assertEqual(v[0], expected_output)

    def test_b_new_entry(self):
        test_data = '3\n3\n3\n3'
        expected_output = {
            "telephone number": "3",
            "name": "3",
            "last name": "3",
            "full name": "3 3",
            "city": "3"
        }
        with patch('sys.stdin', StringIO(test_data)):
            result = new_entry()
            with open('Phonebook.json', 'r') as file:
                result = json.load(file)
                for k, v in result.items():
                    self.assertEqual(v[1], expected_output)
                    self.assertEqual(len(v), 2)

    def test_c_delete_entry(self):
        test_data = '3'
        expected_output = {
            "telephone number": "22",
            "name": "1",
            "last name": "1",
            "full name": "1 1",
            "city": "1"
        }
        with patch('sys.stdin', StringIO(test_data)):
            result = delete_entry()
            with open('Phonebook.json', 'r') as file:
                result = json.load(file)
                for k, v in result.items():
                    self.assertNotIn({
            "telephone number": "3",
            "name": "3",
            "last name": "3",
            "full name": "3 3",
            "city": "3"
        }, v)
                    self.assertEqual(len(v), 1)

    def test_d_search(self):
        test_data = '22'
        expected_output = {
            "telephone number": "22",
            "name": "1",
            "last name": "1",
            "full name": "1 1",
            "city": "1"
        }
        with patch('sys.stdin', StringIO(test_data)):
            self.assertEqual(search(), expected_output)

with open('Phonebook.json', "w") as file:
    txt = {
    "phonebook": [
        {
            "telephone number": "22",
            "name": "3",
            "last name": "3",
            "full name": "3 3",
            "city": "3"
        }
    ]
}
    json.dump(txt, file)

# unittest.main()
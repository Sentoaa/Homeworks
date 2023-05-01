import unittest
from Task1 import *

with open('test.txt', "w") as file:
    txt = "Hello world"
    json.dump(txt, file)


class TestMyCounterTestCase(unittest.TestCase):

    def test_reading(self):
        with MyCounter('test.txt', 'r') as file:
            a = file.read()
        with open('test.txt', 'r') as file:
            b = file.read()
        self.assertEqual(a, b)

    def test_wrighting(self):
        res = "once again hello world"
        with MyCounter('test.txt', 'a+') as file:
            json.dump(res, file)
            a = file.read()
        with open('test.txt', 'a+') as file:
            json.dump(res, file)
            b = file.read()
        self.assertEqual(a, b)

    def test_closing(self):
        with MyCounter('test.txt', 'r') as file:
            a = file.read()
            print(a)
        self.assertTrue(file.closed)

    def test_open_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            open('notexisting_file.txt')


# unittest.main()

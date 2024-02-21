import unittest
from OOP_Exam_program.products import Manual

class TestManual(unittest.TestCase):
    def setUp(self):
        self.manual = Manual(5, "User Manual", "Product Manual", 20, "XYZ Publishing")

    def test_getPublisher(self):
        self.assertEqual(self.manual.getPublisher(), "XYZ Publishing")


import unittest
from OOP_Exam_program.products import Software

class TestSoftware(unittest.TestCase):
    def setUp(self):
        self.software = Software(4, "Office Suite", "Office Software", 100, "123-456")

    def test_getLicense(self):
        self.assertEqual(self.software.getLicense(), "123-456")

if __name__ == '__main__':
    unittest.main()

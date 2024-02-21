import unittest
from OOP_Exam_program.products import Hardware

class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware(3, "Keyboard", "Accessory", 50, 2)

    def test_getWarrantyPeriod(self):
        self.assertEqual(self.hardware.getWarrantyPeriod(), 2)

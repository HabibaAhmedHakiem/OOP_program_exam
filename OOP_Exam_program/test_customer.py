import unittest
from OOP_Exam_program.customers import Company, Individual

class TestCompany(unittest.TestCase):
    def setUp(self):
        self.company = Company(1, "Company", "123456", "Address", "Contact", 0.1)

    def test_getContact(self):
        self.assertEqual(self.company.getContact(), "Contact")

    def test_getDiscount(self):
        self.assertEqual(self.company.getDiscount(), 0.1)


class TestIndividual(unittest.TestCase):
    def setUp(self):
        self.individual = Individual(2, "Individual", "789012", "Another Address", "License123")

    def test_getLicNumber(self):
        self.assertEqual(self.individual.getLicNumber(), "License123")

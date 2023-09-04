"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTestCase(SimpleTestCase):
    def test_addition(self):
        addition = calc.add(3,8)
        self.assertEqual(addition, 11)
    
    def test_substraction(self):
        subst = calc.subst(9989,782)
        self.assertEqual(subst,9207)
from django.test import TestCase

from todo_app.logic import operation


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operation(6, '+', 13)
        self.assertEqual(19, result)

    def test_minus(self):
        result = operation(6, '-', 13)
        self.assertEqual(-7, result)

    def test_multiply(self):
        result = operation(6, '*', 13)
        self.assertEqual(78, result)

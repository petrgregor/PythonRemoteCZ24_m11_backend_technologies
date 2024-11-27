from django.test import TestCase


class ExampleTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: spustí se jednou na začátku a nastaví (vytvoří) testovací data.")

    def setUp(self):
        print("setUp: spustí se před každým testem")

    def test_false(self):
        print("Testovací metoda: test_false")
        result = False
        self.assertFalse(result)

    def test_add(self):
        print("Testovací metoda: test_add")
        result = 1 + 4
        self.assertEqual(result, 5)

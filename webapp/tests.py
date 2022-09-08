from django.test import TestCase

# Create your tests here.
class SampleTest(TestCase):
    def test_sample(self):
        self.assertEqual(1, 1)

    def test_wrong(self):
        self.assertEqual(1, 2)

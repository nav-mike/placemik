from django.test import TestCase
from django.urls import reverse
from .models import Category

# Create your tests here.
class SampleTest(TestCase):
    def test_sample(self):
        self.assertEqual(1, 1)


def create_category(name):
    return Category.objects.create(name=name)


class CategoryIndexViewTests(TestCase):
    def test_no_categories(self):
        """
        If no categories exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("webapp:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No categories are available.")
        self.assertQuerysetEqual(response.context["categories"], [])

    def test_category_list(self):
        """
        Categories are displayed on the index page.
        """
        category = create_category("Test Category")
        response = self.client.get(reverse("webapp:index"))
        self.assertQuerysetEqual(response.context["categories"], [category])

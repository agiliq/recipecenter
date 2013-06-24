from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from recipes.models import Recipe, Category


class SiteTestCase(TestCase):

    def setUp(self):
        self.c = Client()
        self.category = Category(name='Special Filipino Delicacies',
                                 slug='special-filipino-delicacies')
        self.category.save()
        Recipe.objects.create(category=self.category,
                              name='Chiken and Pork Adobo',
                              ingredients='1 cup white or cider vinegar',
                              blah='0',
                              added_by='Ed Pudol',
                              foo='0',
                              bar='4',
                              baz='0',
                              slug='chicken-and-pork-adobo',
                              is_featured=True)

    def test_basepage(self):
        response = self.c.get(reverse("base"))
        self.assertEqual(response.status_code, 200)

    def test_categorypage(self):
        response = self.c.get(reverse("category", args=["special-filipino-delicacies"]))
        self.assertEqual(response.status_code, 200)

    def test_detailpage(self):
        response = self.c.get(reverse("recipe_detail", args=["chicken-and-pork-adobo"]))
        self.assertEqual(response.status_code, 200)


# class SimpleTest(TestCase):
#     def test_basic_addition(self):
#         """
#         Tests that 1 + 1 always equals 2.
#         """
#         self.assertEqual(1 + 1, 2)

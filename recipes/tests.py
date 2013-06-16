"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class SiteTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_startpage(self):
        response = self.c.get(reverse("hello"))
        self.assertEqual(response.status_code, 200)

    def test_basepage(self):
        response = self.c.get(reverse("base"))
        self.assertEqual(response.status_code, 200)


# class SimpleTest(TestCase):
#     def test_basic_addition(self):
#         """
#         Tests that 1 + 1 always equals 2.
#         """
#         self.assertEqual(1 + 1, 2)

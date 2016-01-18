from django.core.urlresolvers import resolve
from django.http.request import HttpRequest
from django.shortcuts import render
from django.test import TestCase

from lists.views import homePage


class HomePageTest(TestCase):
    
    def test_root_url_to_homePage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homePage)

    def test_homePage_returns_correct_HTML(self):
        request = HttpRequest()
        response = homePage(request)
        if response:
            response = response.content.decode('UTF-8')
        expectedHTML = render(request, 'lists/home.html')
        if expectedHTML:
            expectedHTML = expectedHTML.content.decode('UTF-8')
        self.assertEqual(response, expectedHTML)

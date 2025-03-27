from django.test import TestCase, SimpleTestCase
from django.urls import reverse



class HomepageTest(SimpleTestCase):

    def test_url_exist_at_correct_location(self): #تست کردن url ها 
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home-view"))#تست کردن اسمurlها
        self.assertEqual(response.status_code, 200)

    # def test_templates_name(self):
    #     response = self.client.get(reverse("home-view")) تست برای html ها
    #     self.assertTemplateUsed(response, "name.html")

    # def test_templates_content(self):
    #     response = self.client.get("")
    #     self.assertContains(response, "this is test page")تست نویسی برای محتواها
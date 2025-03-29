from django.test import TestCase, SimpleTestCase
from django.urls import reverse



class ProductpagesTest(SimpleTestCase):

    def test_url_exist_at_correct_location(self): #تست کردن url ها 
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
       
    #تست کردن اسمurlها
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home-view"))
        self.assertEqual(response.status_code, 200)

    def test_templates_name(self):
          response = self.client.get(reverse("home-view"))
          self.assertTemplateUsed(response, "home.html")
         
        


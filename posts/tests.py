from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")
    
    def test_model_content(self):
        self.assertEqual(self.post.text,"This is a test!")
        
    
    def test_homepage(self): # new
        response = self.client.get(reverse("home"))
        #checking http status
        self.assertEqual(response.status_code, 200)
        #checking that the correct template is returned
        self.assertTemplateUsed(response, "home.html") 
        #checking that the content has our post
        self.assertContains(response, "This is a test!")

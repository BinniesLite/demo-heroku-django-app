from django.test import TestCase
from django.contrib.auth import get_user_model # reference our active user
from django.urls import reverse

from .models import Post
# Create your tests here.

class BlogTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email ='test@email.com',
            password= 'secret'
        )
        
        self.post = Post.objects.create(
            title='A sample title', 
            body='Bitch cum in me', 
            author=self.user
        )

    def test_string_representation(self): 
        post = Post(title='A sample Title')
        self.assertEqual(str(post), post.title)
    
    def test_post_content(self) -> None:
        self.assertEqual(f'{self.post.title}', 'A sample title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Bitch cum in me')
    
    # Test the home page
    def test_post_list_view(self) -> None:
        response = self.client.get(reverse('home')) # What does this even do?
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Bitch cum in me')
        self.assertTemplateUsed(response, 'home.html')
    
    # They all have to start with test something 
    def test_post_detail_view(self):
        
        response = self.client.get('/post/1')
        no_response = self.client.get('/post/100000/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A sample title') 
        self.assertTemplateUsed(response, 'post_detail.html')
        
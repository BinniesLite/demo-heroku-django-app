from django.test import TestCase, Client
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
        
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A sample title') 
        self.assertTemplateUsed(response, 'post_detail.html')
    
    """
    test_get_absolute url 
    
    
    test to see if it redirect or not
    """
    def test_get_absolute_url(self): 
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')
    
    
    """
    test_post_create_view
    
    
    test to see if it create a post or not
    """
    def test_post_create_view(self):  # new
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title') # does repsone contain a new title
    
        
    """
    test_post_update_view
    
    
    test to see if it edit a post or not
    """
    def test_post_update_view(self): 
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Update title',
            'body': 'cum in me'
        })
        
        self.assertEqual(response.status_code, 302)
    
    def test_post_delete_view(self):
        response = self.client.get(
            reverse('post_delete', args='1')
        )
        
        self.assertEqual(response.status_code, 200)
        
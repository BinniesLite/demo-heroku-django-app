from operator import mod
from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()
    
    # best pracice
    # This added the name to our database? 
    def __str__(self) -> str:
        return self.title
    
    # Specify where to send the user
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)]) # The id is automatically generate
    
    
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title  = models.CharField(max_length = 100, help_text = 'Enter blog title')
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null = True)
    post_date = models.DateField(auto_now_add = True, null=True, blank=True)
    content = models.TextField(null = True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def get_absolute_url(self):
        return reverse('blog-detail', args = [str(self.id)])
    
class Author(models.Model):
    name = models.CharField(max_length = 50)
    profession = models.CharField(max_length=100, help_text = 'Please enter one or more jobs', null=True)
    bio = models.CharField(max_length=200, help_text = 'Write something about yourself', null=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('author-detail', args = [str(self.id)])
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.RESTRICT, null = True)
    comment_body = models.CharField(max_length = 200, help_text = 'Enter your comment')
    post_date = models.DateField(auto_now = True)

    def __str__(self):
        return f'Comment Id - {self.id}, User - {self.user}'
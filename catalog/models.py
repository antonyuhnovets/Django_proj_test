import datetime

from django.db import models
from django.urls import reverse

class Author(models.Model):
    username = models.CharField(max_length=16)
    name = models.CharField(max_length=32)
    email = models.EmailField()
    date_of_birth = models.DateField(null=True)

    def __str__(self): return (f'{self.username}')

    def get_absolute_url(self):
        return reverse('author_list', args=[str(self.id)])

class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=40, help_text='Post title')
    body = models.TextField(max_length=1000, help_text='Post body')
    edit_date = models.DateField(auto_now=True)
    edit_time = models.TimeField(auto_now=True)

    def __str__(self): return f'Post {self.id} from {self.edit_date}'

    def get_absolute_url(self):
        return reverse('post_list', args=[str(self.id)])

# {{ x.get_absolute_url }}



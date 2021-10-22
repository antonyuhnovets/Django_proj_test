from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, UserManager
from django import forms

class Author(User):
    objects = UserManager()
    username = User.username
    email = User.email
    first_name = User.first_name
    last_name = User.last_name

    class Meta:
        proxy = True
        ordering = ('username', 'email', 'first_name', 'last_name')

    def get_absolute_url(self):
        return reverse('author_list', args=[str(self.pk)])

class Post(models.Model):
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=40,)
    body = models.TextField(max_length=1000,)
    edit_date = models.DateField(auto_now=True)
    edit_time = models.TimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post_list', args=[str(self.pk)])



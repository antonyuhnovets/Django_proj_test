from django import forms
from .models import Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea, label_suffix='')
    body = forms.CharField(widget=forms.Textarea, label_suffix='')

    class Meta:
        model = Post
        exclude = ('author', 'edit_date', 'edit_time')

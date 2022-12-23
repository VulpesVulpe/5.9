from django import forms
from .models import *


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'post_title',
           'post_text',
           'category',
           'author'
       ]
       labels = {'post_title': 'Заголовок поста',
                 'post_text': 'Текст поста',
                 'category': 'Категория поста',
                 'author': 'Автор поста'
        }
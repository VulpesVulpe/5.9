from django import forms
from .models import Post


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'post_title',
           'post_text',
           'category',
           'post_author'
       ]
       labels = {'post_title': 'Заголовок поста',
                 'post_text': 'Текст поста',
                 'category': 'Категория поста',
                 'post_author': 'Автор поста'
        }
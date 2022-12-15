from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from datetime import datetime, timezone
from django.core.validators import MinValueValidator
from django.urls import reverse




article = 'AR'
news = 'NW'

POSITIONS = [
    (article, 'Статья'),
    (news, 'Новость')
]

class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        sum_rating = self.post_set.aggregate(post_rating=Sum('post_rating'))
        result_sum_rating = 0
        try:
            result_sum_rating += sum_rating.get('post_rating')
        except TypeError:
            result_sum_rating = 0
        sum_comment_rating = self.author.comment_set.aggregate(comment_rating=Sum('comment_rating'))
        result_sum_comment_rating = 0
        result_sum_comment_rating += sum_comment_rating.get('comment_rating')
        self.author_rating = result_sum_rating * 3 + result_sum_comment_rating
        self.save()


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.category_name.title()


class Post(models.Model):
    post_author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор поста')
    post_choice = models.CharField(max_length=2, choices=POSITIONS, default=news)
    post_date = models.DateField(auto_now_add=True, verbose_name="Дата поста")
    post_category = models.ManyToManyField(Category, through='PostCategory')
    post_title = models.CharField(max_length=90, verbose_name='Заголовок поста')
    post_text = models.TextField(verbose_name='Текст поста')
    post_rating = models.IntegerField(default=0, verbose_name='Рейтинг поста')
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='posts',
    )

    def like(self, amount=1):
        self.post_rating += amount
        self.save()

    def dislike(self, amount=1):
        self.post_rating -= amount
        self.save()

    def preview(self):
        self.post_text = self.post_text[0:124] + '...'
        self.save()

    def __str__(self):
        return f'{self.post_title.title()}: {self.post_text[:100]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self, amount=1):
        self.comment_rating += amount
        self.save()

    def dislike(self, amount=1):
        self.comment_rating -= amount
        self.save()
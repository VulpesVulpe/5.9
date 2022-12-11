1. 
>>> from django.contrib.auth.models import User
>>> user1 = User.objects.create_user('Adam')         
>>> user2 = User.objects.create_user('Eva')  

2. 
>>> from news.models import * 
>>> Author.objects.create(author = user1)
>>> Author.objects.create(author = user2)

3. 
>>> Category.objects.create(category_name = 'ecology')
>>> Category.objects.create(category_name = 'psychology') 
>>> Category.objects.create(category_name = 'sport')   
>>> Category.objects.create(category_name = 'film')    

4. 
>>> Post.objects.create(post_author_id=8, post_choice='AR')
>>> Post.objects.create(post_author_id=9, post_choice='AR') 
>>> Post.objects.create(post_author_id=8, post_choice='NW') 

5. 
>>> Post.objects.get(id=1).post_category.add(Category.objects.get(id=1))
>>> Post.objects.get(id=1).post_category.add(Category.objects.get(id=4))  
>>> Post.objects.get(id=2).post_category.add(Category.objects.get(id=3)) 
>>> Post.objects.get(id=3).post_category.add(Category.objects.get(id=4))

6. 
>>> Comment.objects.create(comment_post=Post.objects.get(id=1),comment_user=Author.objects.get(author_id=9).author,comment_text="It makes you think")
>>> Comment.objects.create(comment_post=Post.objects.get(id=2),comment_user=Author.objects.get(author_id=8).author,comment_text="Fantastic")
>>> Comment.objects.create(comment_post=Post.objects.get(id=3),comment_user=Author.objects.get(author_id=9).author,comment_text="Interesting")

7.
>>> Comment.objects.get(id=1).like()
>>> Post.objects.get(id=1).dislike()
>>> Post.objects.get(id=3).like()

8.
>>> a1=Author.objects.get(author_id=8)
>>> a1.update_rating() 
>>> a1.author_rating
>>> a2=Author.objects.get(author_id=9) 
>>> a2.author.comment_set.aggregate(comment_rating=Sum('comment_rating')) 
>>> a2.update_rating()
>>> a2.author_rating

9.
>>> s = Author.objects.order_by('author_rating')
>>> for i in s:
...     i.author_rating
...     i.author.username

10.
>>> t=Post.objects.order_by('-post_rating')
>>> for i in t[:1]:
...     i.post_date
...     i.post_rating
...     i.post_author.author
...     i.post_title
...     i.preview()

11.
>>> Post.objects.all().order_by('-post_rating')[0].comment_set.values(
... 'comment_date','comment_user','comment_rating','comment_text')

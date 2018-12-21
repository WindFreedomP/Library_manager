from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogArticle(models.Model):
    title=models.CharField(max_length=300)
    author=models.ForeignKey(User,related_name="blog_posts",on_delete=models.CASCADE)
    body=models.TextField()

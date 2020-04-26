from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Article(models.Model):
    """
    Data Model representing an article of our blog
    """
    class Meta:
        ordering = ['-created']

    slug = models.SlugField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)

    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    def __str__(self):
        return self.title

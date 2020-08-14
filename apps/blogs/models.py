from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    STATUS_DRAFT = 0
    STATUS_PUBLISH = 1
    STATUS = (
        (STATUS_DRAFT, "Draft"),
        (STATUS_PUBLISH, "Publish")
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=STATUS_DRAFT)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title

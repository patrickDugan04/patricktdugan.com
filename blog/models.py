from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image_url = models.TextField(default="https://i.kym-cdn.com/photos/images/facebook/001/430/011/c1d.png")
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

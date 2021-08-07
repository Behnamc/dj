from django.db import models
from django.db.models.fields import DateTimeField, TextField

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = TextField()
    date = DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg',blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'
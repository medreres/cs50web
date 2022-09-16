from django.contrib.auth.models import AbstractUser
from django.db import models
from project4.settings import POSTLENGTH


class User(AbstractUser):
    followers = models.ManyToManyField('self', related_name='follower', blank=True, symmetrical=False)
    following = models.ManyToManyField('self', related_name='follow', blank=True, symmetrical=False)
    liked = models.ManyToManyField('Post', related_name='like', blank=True)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=POSTLENGTH)
    timestamp = models.DateTimeField()
    likes = models.ManyToManyField('User', related_name='likes', blank=True)

    def serialize(self):
        return {
            "id": self.id,
            'username': self.author.username,
            "body": self.body,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            'likes': self.likes.count()
        }

    def __str__(self):
        return f'Author: {self.author}: {self.body}'

from pyexpat import model
from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.db import models
from httplib2 import Authentication
from commerce.settings import CATEGORIESCHOICES


class User(AbstractUser):
    WatchListSize = models.PositiveIntegerField(default=0)


class AuctionListing(models.Model):
    author = models.ForeignKey(
        User, models.CASCADE, null=True, related_name="author")
    title = models.CharField(max_length=256)
    description = models.CharField(
        max_length=256, default='', null=True, blank=True)
    date = models.DateTimeField()
    price = models.FloatField()
    image = models.URLField(blank=True)
    category = models.CharField(
        max_length=256, blank=True, choices=CATEGORIESCHOICES)
    isClosed = models.BooleanField(default=False)
    winner = models.ForeignKey(
        User, models.CASCADE, null=True, related_name="winner", blank=True)


class Bid(models.Model):
    author = models.ForeignKey(User, models.CASCADE, null=True)
    listing = models.ForeignKey(AuctionListing, models.CASCADE, default=1)
    price = models.FloatField()
    date = models.DateField()


class Comment(models.Model):
    author = models.ForeignKey(User, models.CASCADE, null=True)
    listing = models.ForeignKey(AuctionListing, models.CASCADE, null=True)
    text = models.CharField(max_length=256)


class WatchList(models.Model):
    author = models.ForeignKey(User, models.CASCADE, null=True)
    listing = models.ForeignKey(AuctionListing, models.CASCADE, null=True)

# Generated by Django 4.0.5 on 2022-07-13 07:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auctionlisting_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='WatchList',
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='WatchList',
            field=models.ManyToManyField(blank=True, related_name='WatchList', to=settings.AUTH_USER_MODEL),
        ),
    ]

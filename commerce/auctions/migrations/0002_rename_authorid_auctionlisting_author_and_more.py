# Generated by Django 4.0.5 on 2022-07-12 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionlisting',
            old_name='authorId',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='authorId',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='authorId',
            new_name='author',
        ),
    ]

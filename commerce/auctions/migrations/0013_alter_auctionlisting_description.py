# Generated by Django 4.0.5 on 2022-07-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_auctionlisting_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='description',
            field=models.CharField(blank=True, default='', max_length=256, null=True),
        ),
    ]

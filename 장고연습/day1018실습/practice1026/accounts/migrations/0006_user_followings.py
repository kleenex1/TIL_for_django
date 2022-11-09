# Generated by Django 3.2.13 on 2022-10-25 05:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_review_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]

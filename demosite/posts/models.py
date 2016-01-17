from __future__ import unicode_literals
from django.db import models


class Post(models.Model):
    article = models.ForeignKeyField('articles.Article')
    user = models.ForeignKeyField('auth.User')
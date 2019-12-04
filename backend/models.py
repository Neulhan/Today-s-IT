from django.db import models

# Create your models here.


class News(models.Model):
    title = models.TextField()
    content = models.TextField(default='')
    url = models.TextField(default='')
    reference = models.TextField(default='')
    written_date = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)


class KeyWord(models.Model):
    key = models.TextField()
    count = models.IntegerField()


class AllContent(models.Model):
    text = models.TextField()

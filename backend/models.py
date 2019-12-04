from django.db import models

# Create your models here.


class News(models.Model):
    title = models.TextField()
    content = models.TextField(default='')
    exposed_sequence = models.IntegerField(default=0)
    url = models.TextField(default='')
    main_key_word = models.TextField(default='')
    reference = models.TextField(default='')
    written_date = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)


class KeyWord(models.Model):
    key = models.TextField()
    count = models.IntegerField()


class AllContent(models.Model):
    text = models.TextField()

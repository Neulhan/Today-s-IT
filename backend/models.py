from django.db import models


class News(models.Model):
    title = models.TextField()
    content = models.TextField(default='')
    url = models.TextField(default='')
    reference = models.TextField(default='')
    written_date = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class KeyWord(models.Model):
    name = models.CharField(max_length=20)
    count = models.IntegerField(default=0)
    key_from = models.ManyToManyField(News)

    class Meta:
        ordering = ('-count', 'name')

    def __str__(self):
        return self.name


class AllContent(models.Model):
    text = models.TextField()

    def __str__(self):
        return "모든 뉴스 내용을 모은 덩어리"

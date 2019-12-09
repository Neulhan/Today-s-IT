from django.contrib import admin

# Register your models here.
from backend.models import News, KeyWord, AllContent, KeyWordHistory

admin.site.register(News)
admin.site.register(KeyWord)
admin.site.register(AllContent)
admin.site.register(KeyWordHistory)

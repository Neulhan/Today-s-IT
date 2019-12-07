from django.contrib import admin

# Register your models here.
from backend.models import News, KeyWord, AllContent

admin.site.register(News)
admin.site.register(KeyWord)
admin.site.register(AllContent)

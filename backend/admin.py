from django.contrib import admin

# Register your models here.
from backend.models import News, KeyWord, AllContent, KeyWordHistory

admin.site.register(KeyWord)
admin.site.register(AllContent)
admin.site.register(KeyWordHistory)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'written_date']
    list_display_links = ['id', 'title']


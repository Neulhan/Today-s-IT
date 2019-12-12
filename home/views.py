from django.shortcuts import render

# Create your views here.
from backend.models import News, KeyWord, KeyWordHistory


def home(request):
    return render(request, 'home/home.html')


def news_all(request):
    return render(request, 'home/news_all.html', {'news': News.objects.all().order_by('-written_date'),
                                                  'keywords': KeyWord.objects.all(),
                                                  'keywords_h': KeyWordHistory.objects.all()})

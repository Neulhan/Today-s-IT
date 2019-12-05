from backend.crawler.crawling_settings import *
# from backend.models import News
from backend.models import News


def crawling():
    print('크롤링 시작점')
    reference = '테크니들'
    url = 'http://techneedle.com/'
    print('크롤링 시작점2')
    html = requests.get(url).text
    print(html)
    soup = bs(html, 'html.parser')
    news_list = soup.select('.entry-title > a')
    print(news_list)
    for news in news_list:
        print(news.text)
        title = news.text
        # check = News.objects.filter(title=title)
        if title == 0:
            pass
        else:
            if News.objects.filter(title=title):
                continue
            url = news.get('href')
            html = requests.get(url).text
            soup = bs(html, 'html.parser')
            content = soup.select('.entry-content')[0].text.replace('\n', '')
            time = soup.select('time')[0].get('datetime').split('T')[0].replace('-', '')
            News.objects.create(title=title,
                                content=content,
                                written_date=time,
                                url=url,
                                reference=reference)
    print('크롤링 끝점')
    return 0
    # title = models.TextField()
    # content = models.TextField()
    # exposed_sequence = models.IntegerField()
    # url = models.TextField()
    # main_key_word = models.TextField()
    # reference = models.TextField()
    # written_date = models.DateTimeField()
    # created_at = models.DateTimeField(auto_now_add=True)


if __name__ == '__main__':
    crawling()

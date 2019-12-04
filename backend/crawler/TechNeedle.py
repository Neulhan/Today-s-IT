from backend.crawler.crawling_settings import *
# from backend.models import News


def crawling():
    reference = '테크니들'
    url = 'http://techneedle.com/'
    html = requests.get(url).text
    soup = bs(html, 'html.parser')
    news_list = soup.select('.entry-title > a')
    counter = 1
    for news in news_list:
        title = news.text
        # check = News.objects.filter(title=title)
        if title == 0:
            pass
        else:
            url = news.get('href')
            html = requests.get(url).text
            soup = bs(html, 'html.parser')
            content = soup.select('.entry-content')[0].text
            time = soup.select('time')[0].get('datetime').split('T')[0].replace('-', '')

            counter += 1
            break

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

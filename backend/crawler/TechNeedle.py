from backend.crawler.crawling_settings import *
# from backend.models import News
from backend.models import News, AllContent, KeyWord


def crawling():
    print('크롤링 시작점')
    nlp = Okt()
    reference = '테크니들'
    url = 'http://techneedle.com/'
    print('크롤링 시작점2')
    html = requests.get(url).text
    soup = bs(html, 'html.parser')
    news_list = soup.select('.entry-title > a')
    print(news_list)
    for news in news_list:
        title = news.text
        # check = News.objects.filter(title=title)
        if title == 0:
            pass
        else:
            try:
                News.objects.get(title=title)
            except Exception as e:
                title_10 = title*10
                url = news.get('href')
                html = requests.get(url).text
                soup = bs(html, 'html.parser')
                content = soup.select('.entry-content')[0].text.replace('\n', '')
                time = soup.select('time')[0].get('datetime').split('T')[0].replace('-', '')
                created_news_obj = News.objects.create(title=title,
                                                       content=content,
                                                       written_date=time,
                                                       url=url,
                                                       reference=reference)

                nouns = nlp.nouns(content+title_10)
                count = Counter(nouns)
                print(count.most_common(5))
                for item in count.most_common(5):
                    word = item[0]
                    number = item[1]
                    keyword_obj = KeyWord.objects.get_or_create(name=word)[0]
                    print(keyword_obj)
                    origin_count = keyword_obj.count
                    print(origin_count)
                    print(type(origin_count))
                    keyword_obj.count = origin_count + number
                    keyword_obj.key_from.add(created_news_obj)
                    keyword_obj.save()

    print('크롤링 끝점')


if __name__ == '__main__':
    crawling()


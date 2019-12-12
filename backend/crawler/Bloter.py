from backend.crawler.crawling_settings import *
# from backend.models import News
from backend.models import News, AllContent, KeyWord


def crawling():
    print('크롤링 시작 : Bloter')
    nlp = Okt()
    reference = 'Bloter'
    url = 'http://www.bloter.net/archives/category/contents'

    html = requests.get(url).text
    soup = bs(html, 'html.parser')
    news_list = soup.select('div > .general-article--title > a')

    for news_num, news in enumerate(news_list, 1):
        title = news.text
        print(f'({news_num}/{len(news_list)}) {title} 작업중')
        # check = News.objects.filter(title=title)
        if title == 0:
            pass
        else:
            try:
                News.objects.get(title=title)
            except Exception as e:
                title_5 = title * 5
                url = news.get('href')
                html = requests.get(url).text
                soup = bs(html, 'html.parser')

                content = soup.select('div.article--body__wrapper div.article--content')
                try:
                    content = content[0].text.replace('\n', '')
                except IndexError:
                    content = soup.select('div.entry-content')[0].text.replace('\n', '')

                time = soup.select('#sidebar--widget--top > div.article--date.widget--row > .publish')

                try:
                    time = time[0].text
                except IndexError:
                    time = soup.select('div.entry-title-container .date')[0].text
                time = time.replace('.', '')

                created_news_obj = News.objects.create(title=title,
                                                       content=content,
                                                       written_date=time,
                                                       url=url,
                                                       reference=reference)

                nouns = nlp.nouns(content + title_5)
                count = Counter(nouns)

                for item in count.most_common(5):
                    word = item[0]
                    number = item[1]
                    if word in except_list:
                        pass
                    else:
                        keyword_obj = KeyWord.objects.get_or_create(name=word)[0]

                        origin_count = keyword_obj.count

                        keyword_obj.count = origin_count + number
                        keyword_obj.key_from.add(created_news_obj)
                        keyword_obj.save()

    print('크롤링 끝 : Bloter')


if __name__ == '__main__':
    crawling()

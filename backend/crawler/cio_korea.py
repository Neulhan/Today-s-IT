from backend.crawler.crawling_settings import *
# from backend.models import News
from backend.models import News, AllContent, KeyWord


def crawling():
    print('크롤링 시작 : CIO Korea')
    nlp = Okt()
    reference = 'CIO Korea'
    url = 'http://www.ciokorea.com/news'

    html = requests.get(url).text
    soup = bs(html, 'html.parser')

    news_list = soup.select('div.container  div.contents-body  h4.news_list_full_size > a')

    for news_num, news in enumerate(news_list, 1):
        title = news.text
        url = 'http://www.ciokorea.com/' + news.get('href')

        print(f'({news_num}/{len(news_list)}) {title} 작업중')
        try:
            News.objects.get(title=title)
        except Exception as e:
            html = requests.get(url).text
            soup = bs(html, 'html.parser')
            time = datetime.datetime.now()
            if len(str(time.month)) < 2:
                month = f'0{time.month}'
            else:
                month = time.month
            if len(str(time.day)) < 2:
                day = f'0{time.day}'
            else:
                day = time.day

            time = f'{time.year}{month}{day}'

            content = soup.select('div.container  div.contents-body div.node_body.cb')[0].text.replace('<br/>', '')

            created_news_obj = News.objects.create(title=title,
                                                   content=content.replace('\n', ''),
                                                   written_date=time,
                                                   url=url,
                                                   reference=reference)

            nouns = nlp.nouns(content + title*5)
            count = Counter(nouns)

            for item in count.most_common(5):
                word = item[0]
                number = item[1]

                if word in except_list:
                    pass

                else:
                    try:
                        keyword_obj = KeyWord.objects.get_or_create(name=word)[0]

                        origin_count = keyword_obj.count

                        keyword_obj.count = origin_count + number

                        keyword_obj.key_from.add(created_news_obj)

                        keyword_obj.save()
                    except Exception as e:
                        print(e)



    print('크롤링 끝 : CIO Korea')


if __name__ == '__main__':
    crawling()


from backend.crawler.crawling_settings import *
# from backend.models import News
from backend.models import News, AllContent, KeyWord


def crawling(driver):
    print('크롤링 시작 : ZDNet')
    nlp = Okt()
    reference = 'ZDNet'
    url = 'http://www.zdnet.co.kr/news/?lstcode=0020&page=1'
    driver.get(url)

    req = driver.page_source
    soup = bs(req, 'html.parser')

    news_list = soup.select('.news_box > .newsPost > .assetText > a')

    for news_num, news in enumerate(news_list, 1):
        detail_url = f'http://www.zdnet.co.kr/{news.get("href")}'
        title = news.select('h3')[0].text
        print(f'({news_num}/{len(news_list)}) {title} 작업중')
        try:
            News.objects.get(title=title)
        except Exception as e:
            driver.get(detail_url)
            req = driver.page_source

            soup = bs(req, 'html.parser')

            summary = soup.select('div.container  div.news_head > p')[0].text

            content_list = soup.select('#content > p')

            content = ''

            for i in content_list:
                content += i.text
            time = soup.select('div.news_head > div > p > span')[0].text[4:14].replace('/', '')
            created_news_obj = News.objects.create(title=title,
                                                   content=content,
                                                   written_date=time,
                                                   url=url,
                                                   reference=reference)

            nouns = nlp.nouns(content + title*5 + summary*5)
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

        if news_num == 5:
            break
    print('크롤링 끝 : ZDNet')


if __name__ == '__main__':
    crawling()


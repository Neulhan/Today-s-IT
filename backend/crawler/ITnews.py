from backend.crawler.crawling_settings import *
# from backend.models import News
from backend.models import News, AllContent, KeyWord


def crawling():
    print('크롤링 시작 : ITNews')
    nlp = Okt()
    reference = 'ITNews'
    url = 'http://www.itnews.or.kr'

    html = requests.get(url).text
    soup = bs(html, 'html.parser')
    news_list = soup.select('div.item-details > h3 > a')

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

                content = soup.select('div.td-post-content')[0].text.replace('\n', '')
                all_time = ''
                time = soup.select('div.td-post-header time')[0].text.replace('년', '').replace('월', '').replace('일',
                                                                                                                '').replace(
                    ' ', '')
                if len(time) < 8:
                    time = list(time)
                    time = time[:6] + ['0'] + list(time[-1])

                    for i in time:
                        all_time += i

                    time = all_time

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

    print('크롤링 끝 : ITNews')


if __name__ == '__main__':
    crawling()
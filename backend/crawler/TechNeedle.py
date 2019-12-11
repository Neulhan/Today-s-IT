from backend.crawler.crawling_settings import *
# from backend.models import News
from backend.models import News, AllContent, KeyWord


def crawling():
    print('크롤링 시작 : TechNeedle')
    nlp = Okt()
    reference = '테크니들'
    url = 'http://techneedle.com/'

    html = requests.get(url).text
    soup = bs(html, 'html.parser')
    news_list = soup.select('.post-inside .entry-title > a')

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
                title_5 = title*5
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

                nouns = nlp.nouns(content+title_5)
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

    print('크롤링 끝 : TechNeedle')


if __name__ == '__main__':
    crawling()

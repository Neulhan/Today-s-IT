# from backend.crawler.crawling_settings import *
# # from backend.models import News
# from backend.models import News, AllContent, KeyWord
#
#
# def crawling():
#     print('크롤링 시작 : 디지털데일리')
#     nlp = Okt()
#     reference = '디지털데일리'
#     url = 'http://www.ddaily.co.kr/news/article_list_all/'
#
#     html = requests.get(url).text
#     soup = bs(html, 'html.parser')
#     news_list = soup.select('#container div.section_h12sub  dl')
#
#     for news_num, news in enumerate(news_list, 1):
#         title = news.select('a')[0].text
#         url = 'http://www.ddaily.co.kr/' + news.select('a')[0].get('href')
#         print(f'({news_num}/{len(news_list)}) {title} 작업중')
#
#         try:
#             News.objects.get(title=title)
#         except Exception as e:
#             html = requests.get(url).text
#             soup = bs(html, 'html.parser')
#             print(soup)
#             content = soup.select('div.article--body__wrapper div.article--content')
#             print('임시끝')
#             break
            #
            # created_news_obj = News.objects.create(title=title,
            #                                        content=content,
            #                                        written_date=time,
            #                                        url=url,
            #                                        reference=reference)
            #
            # nouns = nlp.nouns(content + title*5)
            # count = Counter(nouns)
            #
            # for item in count.most_common(5):
            #     word = item[0]
            #     number = item[1]
            #     if word in except_list:
            #         pass
            #     else:
            #         keyword_obj = KeyWord.objects.get_or_create(name=word)[0]
            #
            #         origin_count = keyword_obj.count
            #
            #         keyword_obj.count = origin_count + number
            #         keyword_obj.key_from.add(created_news_obj)
            #         keyword_obj.save()

#     print('크롤링 끝 : 디지털데일리')
#
#
# if __name__ == '__main__':
#     crawling()
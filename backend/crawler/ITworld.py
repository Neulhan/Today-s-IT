from backend.crawler.crawling_settings import *


def crawling():
    url = 'http://www.itworld.co.kr/news'
    html = requests.get(url).text
    soup = bs(html, 'html.parser')
    news_list = soup.select('.news_list_sub_list_cb')

    return 0


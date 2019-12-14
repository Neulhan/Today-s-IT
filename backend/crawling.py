from backend.models import KeyWord, KeyWordHistory
from .crawler.ITnews import crawling as it_news_crawling
from .crawler.ITworld import crawling as it_world_crawling
from .crawler.Kbench import crawling as k_bench_crawling
from .crawler.Naver import crawling as naver_crawling
from .crawler.TechNeedle import crawling as tech_needle_crawling
from .crawler.ZDNet import crawling as zd_net_crawling
from .crawler.Bloter import crawling as bloter_crawling
# from .crawler.digital_daily import crawling as digital_daily_crawling
from .crawler.cio_korea import crawling as cio_korea_crawling
from selenium import webdriver


def run_driver():
    # 웹 드라이버 설치 http://chromedriver.chromium.org/downloads
    # 웹 드라이버 경로 지정

    path = 'static/chromedriver.exe'
    driver = webdriver.Chrome(path)
    return driver


def crawling_tech_needle():
    # tech_needle_crawling()
    bloter_crawling()
    it_news_crawling()
    cio_korea_crawling()

    # digital_daily_crawling()

    # driver = run_driver()
    # zd_net_crawling(driver)


def keyword_initialize():
    keys = KeyWord.objects.all()
    for key in keys:
        key_history_obj = KeyWordHistory.objects.create(
            name=key.name,
            count=key.count
        )
        for news in key.key_from.all():
            key_history_obj.key_from.add(news)
    print("키워드 전환 완료")
    keys.delete()
    print("기존 키워드 삭제")

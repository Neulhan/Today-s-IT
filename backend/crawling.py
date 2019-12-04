from .crawler.ITnews import crawling as it_news_crawling
from .crawler.ITworld import crawling as it_world_crawling
from .crawler.Kbench import crawling as k_bench_crawling
from .crawler.Naver import crawling as naver_crawling
from .crawler.TechNeedle import crawling as tech_needle_crawling
from .crawler.ZDNet import crawling as zd_net_crawling


def crawling_all():
    # it_news_crawling()
    # it_world_crawling()
    # k_bench_crawling()
    # naver_crawling()
    tech_needle_crawling()
    # zd_net_crawling()

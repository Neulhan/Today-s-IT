from datetime import datetime

from django.core.management import BaseCommand, CommandError

from backend.crawling import crawling_tech_needle, keyword_initialize


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(f"{datetime.now()} keyword_initialize 실행중...")
        keyword_initialize()
        print(f"{datetime.now()} keyword_initialize 실행완료")
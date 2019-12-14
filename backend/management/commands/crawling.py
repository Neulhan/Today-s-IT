from datetime import datetime

from django.core.management import BaseCommand, CommandError

from backend.crawling import crawling_tech_needle


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(f'{datetime.now()}크롤링 실행중...'))
        crawling_tech_needle()
        self.stdout.write(self.style.SUCCESS(f'{datetime.now()}크롤링 실행완료'))


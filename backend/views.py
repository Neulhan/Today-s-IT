from datetime import datetime

import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from backend.crawling import *

import pandas as pd
import numpy as np

from backend.models import News, AllContent, KeyWord, KeyWordHistory
from backend.serializers import NewsSerializer, KeywordSerializer


class NewsList(APIView):
    def get(self, request):
        s = NewsSerializer(News.objects.all(), many=True)
        data = {}
        data['news'] = s.data

        # self.crawling(request)
        return Response(data)


class NewsCrawlingTechNeedle(APIView):
    def get(self, request):
        crawling_tech_needle()
        return Response(123)


class GetAllContent(APIView):
    def get(self, request):
        s = NewsSerializer(AllContent.objects.get(id=1))
        data = {}
        data['content_all'] = s.data

        return Response(data)


class GetNewsByKeyword(APIView):
    def get(self, request, pk):
        keyword_obj = KeyWord.objects.get(name=pk)
        response_query = keyword_obj.key_from.all()
        s = NewsSerializer(response_query, many=True)
        data = {}
        data['key_from'] = s.data

        return Response(data)


class GetKeywordRank(APIView):
    def get(self, request):
        response_query = KeyWord.objects.all()[:10]
        s = KeywordSerializer(response_query, many=True)
        data = {}
        data['keyword_rank'] = s.data

        return Response(data)


class KeyWordInitialization(APIView):
    def get(self, request):
        keys = KeyWord.objects.all()
        for key in keys:
            key_history_obj = KeyWordHistory.objects.create(
                name=key.name,
                count=key.count
            )
            for news in key.key_from.all():
                key_history_obj.key_from.add(news)

        keys.delete()
        return Response(100)


class Delete(APIView):
    def get(self, request):
        KeyWord.objects.all().delete()
        News.objects.all().delete()
        KeyWordHistory.objects.all().delete()
        return Response(100)
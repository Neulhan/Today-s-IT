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

from backend.models import News
from backend.serializers import NewsSerializer


class NewsList(APIView):
    def get(self, request):
        s = NewsSerializer(News.objects.all(), many=True)
        data = {}
        data['테크니들'] = s.data

        # self.crawling(request)
        return Response(data)


class NewsCrawlingTechNeedle(APIView):
    def get(self, request):
        print(1, datetime.now())
        crawling_tech_needle()
        print(2, datetime.now())
        return Response(123)

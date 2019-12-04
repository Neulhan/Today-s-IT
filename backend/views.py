from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from backend.crawling import crawling_all

import pandas as pd
import numpy as np

from backend.models import News
from backend.serializers import NewsSerializer


class NewsList(APIView):

    # def crawling(self, request):
    #     crawling_all()
    #     return Response()

    def get(self, request):
        np_obj = np.random.rand(10, 2)
        for i in np_obj:
            News.objects.create(title=str(i[0]), content=str(i[1]))
        s = NewsSerializer(News.objects.all(), many=True)
        data = json.dumps({'pets': s.data})

        # self.crawling(request)
        return Response(data)

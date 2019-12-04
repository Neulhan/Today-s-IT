from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.crawling import crawling_all


class NewsList(APIView):

    def crawling(self):
        crawling_all()
        return Response()

    def get(self, request):
        self.crawling()
        return Response()

from django.urls import path

from backend import views

urlpatterns = [
    path('', views.NewsList.as_view()),
    path('crawling/', views.NewsCrawlingTechNeedle.as_view()),
    path('news/<str:pk>/', views.GetNewsByKeyword.as_view()),
    path('keyword-rank/', views.GetKeywordRank.as_view()),
    path('keyword-rank/<str:date>/', views.GetKeywordRankByDate.as_view()),
    path('keyword-initialization/', views.KeyWordInitialization.as_view()),
    path('del/', views.Delete.as_view()),
]

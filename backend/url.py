from django.urls import path

from backend import views

urlpatterns = [
    path('', views.NewsList.as_view()),
    path('crawling/', views.NewsCrawlingTechNeedle.as_view()),
    path('news/<str:pk>/', views.GetNewsByKeyword.as_view())
]

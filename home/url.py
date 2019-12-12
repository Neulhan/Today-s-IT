from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.news_all, name='all'),
]

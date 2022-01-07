from django.shortcuts import render
from news.models import News


#  главная страница приложения.
def index(request):
    news = News.objects.all()
    return render(request, "index.html", {"news": news})


#  полная информация о новости
def news_detail(request, news_pk):
    news = News.objects.get(id=news_pk)
    return render(request, 'news_detail.html', {'news': news})
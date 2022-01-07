from django.shortcuts import render
from news.models import News
from django.http import HttpResponse
from django.core.cache import cache


#  главная страница приложения.
def index(request):
    cache_news = "news"
    # если в Redis есть такой ключ, забираем значение по ключю из кеша
    if cache.get(cache_news):
        news = cache.get("news")
        print("hit the cache")
    else:
        # если в кеше Redis нет ключа, записывем его в кеш.
        try:
            news = News.objects.all()
            # timeout=10 - время жизни ключа 10 секунд
            cache.set("news", news, timeout=10)
            print("hit the db")
        except News.DoesNotExist:
            return HttpResponse("this recipe does not exist")
    return render(request, "index.html", {"news": news})


#  полная информация о новости
def news_detail(request, news_pk):
    if cache.get(news_pk):
        print("data from cache")
        news = cache.get(news_pk)
    else:
        print("data from DB")
        news = News.objects.get(id=news_pk)
        cache.set(news_pk, news, timeout=10)
    return render(request, 'news_detail.html', {'news': news})






# WITHOUT CACHE
#  полная информация о новости
# def news_detail(request, news_pk):
#     news = News.objects.get(id=news_pk)
#     return render(request, 'news_detail.html', {'news': news})


# главная страница приложения.
# def index(request):
#     news = News.objects.all()
#     return render(request, "index.html", {"news": news})


# import redis
#
# r = redis.Redis()

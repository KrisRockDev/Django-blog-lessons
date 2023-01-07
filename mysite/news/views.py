from django.shortcuts import render
from django.http import HttpResponse
from .models import News
def index(request):
    news = News.objects.all()
    res = '<h1>Список новостей</h1>\n<hr>\n'
    for item in news:
        res += f'<div>\n<p><h3>{item.title}</h3></p>\n<p>{item.content}</p>\n<div>\n<hr>\n'
    return HttpResponse(res)

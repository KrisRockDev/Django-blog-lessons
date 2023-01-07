from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    news = News.objects.all()
    return render(
        request=request,
        template_name='news/index.html',
        context={
            'news': news,
            'title': 'Новостной портал',
        },
    )

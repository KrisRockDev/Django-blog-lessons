from django.shortcuts import render
from .models import News, Category


def index(request):
    news = News.objects.all()
    cat_count = {}

    CONTEXT = {
        'news': news,
        'cat_count': cat_count,
        'title': 'Новостной портал',
    }

    return render(
        request=request,
        template_name='news/index.html',
        context=CONTEXT,
    )


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    CONTEXT = {
        'news': news,
        'category': category,
        'title': 'Новостной портал',
    }

    return render(
        request=request,
        template_name='news/category.html',
        context=CONTEXT,
    )


def view_news(request, news_id):
    view_news = News.objects.get(pk=news_id)

    CONTEXT = {
        'view_news_item': view_news,
        'title': 'Новостной портал',
    }

    return render(
        request=request,
        template_name='news/view_news.html',
        context=CONTEXT,
    )

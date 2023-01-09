from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    cat_count = {}

    CONTEXT = {
        'news': news,
        'categories': categories,
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
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)

    CONTEXT = {
        'news': news,
        'categories': categories,
        'category': category,
        'title': 'Новостной портал',
    }

    return render(
        request=request,
        template_name='news/category.html',
        context=CONTEXT,
    )

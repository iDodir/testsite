from django.shortcuts import render

from django.http import HttpResponse

from .models import News, Category


# Create your views here.

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id: int):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, template_name='news/category.html',
                  context={'news': news, 'category': category})

from django.shortcuts import render
from .models import News


def news_view(request):
    news = News.objects.all()

    return render(request, 'app/index.html', {'news': news})


def news_detail(request, pk):
    news = News.objects.get(id=pk)

    return render(request, 'app/news_detail.html', {'news': news})


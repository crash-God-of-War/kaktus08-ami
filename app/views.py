from django.shortcuts import render
from .models import News


def news_view(request):
    news = News.objects.all()

    return render(request, 'app/index.html', {'news': news})


def news_detail(request, pk):
    news = News.objects.get(id=pk)

    return render(request, 'app/news_detail.html', {'news': news})


def news_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        descriptions = request.POST['descriptions']
        category = request.POST['category']
        image = request.FILES['image']
        video = request.FILES['video']
        music = request.FILES['music']

        news = News(
            title=title,
            descriptions=descriptions,
            category=category,
            image=image,
            video=video,
            music=music,
        )
        news.save()

    return render(request, 'app/News_create.html')

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=228)
    description = models.TextField()

    class News(models.Model):
        category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/new_images', blank=True, mull=True)
    video = models.FileField(upload_to='media/news_video', blank=True, mull=True)
    audio = models.FileField(upload_to='media/news_audio', blank=True, mull=True)

    def __str__(self):
        return self.title

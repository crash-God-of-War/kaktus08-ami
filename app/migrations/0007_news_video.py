# Generated by Django 5.0.6 on 2024-06-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='video',
            field=models.FileField(default=1, upload_to='media/news_video'),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_news_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='audio',
            field=models.FileField(default=1, upload_to='media/news_audio'),
            preserve_default=False,
        ),
    ]

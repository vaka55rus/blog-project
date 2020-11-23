# Generated by Django 3.1.2 on 2020-11-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articlesapp', '0004_auto_20201117_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='articleid',
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='articlesapp.Category', verbose_name='Категории статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name='Содержание статьи'),
        ),
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Опубликовать да\\нет'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Заголовок статьи'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=300, verbose_name='Имя категории'),
        ),
    ]

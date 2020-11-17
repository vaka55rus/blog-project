from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Category(models.Model):
    category = models.CharField(max_length=300)
    articleid = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        null = True,
    )

    def __str__(self):
        return self.category
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Category(models.Model):
    category = models.CharField(max_length=300)

    def __str__(self):
        return self.category

class Article(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    author = models.OneToOneField(
        Author,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    date_create = models.DateTimeField()
    date_modification = models.DateTimeField()
    published = models.BooleanField(null=True)

    def __str__(self):
        return self.title
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class FilmRegistration(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="category_movie",
        blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    cover = models.FileField(upload_to='cover')
    duration = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

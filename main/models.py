from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)




class Films(models.Model):
    title = models.CharField('Title', max_length=50)
    genre = models.CharField('Genre', max_length=20)
    desc = models.TextField("Description")
    rating = models.IntegerField("Rating")
    image = models.ImageField("Image", upload_to='img/')
    categoryID = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Film",
        verbose_name_plural = "Films"



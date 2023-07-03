from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=600, null=True, blank=True)
    key = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='images', null=True)
    def __str__(self):
        return self.title
    
class NewCategorie(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class New(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images')
    pub_date = models.DateField(default=timezone.now)
    category = models.ForeignKey(to=NewCategorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Historie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='history_images')
    history_title = models.CharField(max_length=200)
    history_description = models.TextField()
    history_image = models.ImageField(upload_to='history_images')
    street = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title
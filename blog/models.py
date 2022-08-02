from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='blog_images/', blank=True)

    def __str__(self):
        return self.title
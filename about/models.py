from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class AboutPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f"{self.title} by {self.author}"


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"

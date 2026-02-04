from django.db import models

# Create your models here.


class AboutPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} by {self.author}"

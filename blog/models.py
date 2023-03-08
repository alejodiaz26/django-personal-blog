from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creation_date"]

    def __str__(self):
        return self.title
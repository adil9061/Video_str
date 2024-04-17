from django.db import models
from django.contrib.auth.models import AbstractUser
import cv2

# Create your models here.

class CustomUser(AbstractUser):

    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Video(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.name




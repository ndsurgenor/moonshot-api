from django.db import models
from django.contrib.auth.models import User
import datetime
from .variables import MAIN_FEATURES


class Photo(models.Model):
    """
    Creates a photo model instance connected to a specific user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=127)
    main_feature = models.CharField(
        max_length=127, choices=MAIN_FEATURES
    )    
    location = models.CharField(max_length=127)    
    description = models.TextField(blank=True)
    photo_date = models.DateField(default=datetime.date.today)
    photo_time = models.TimeField(blank=True)
    lens_used = models.CharField(max_length=127, blank=True)
    camera_used = models.CharField(max_length=127, blank=True)
    other_equipment_used = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default = '../default_photo',
    )


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}, {self.created_at} by {self.user}'
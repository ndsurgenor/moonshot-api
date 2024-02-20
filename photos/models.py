from django.db import models
from django.contrib.auth.models import User
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
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=127)
    photo_date = models.DateField(blank=True, null=True)
    photo_time = models.TimeField(blank=True, null=True)
    lens_used = models.CharField(
        max_length=127,
        blank=True,
        null=True
    )
    camera_used = models.CharField(
        max_length=127,
        blank=True,
        null=True
    )
    other_equipment_used = models.TextField(
        max_length=127,
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='images/',
        default = '../default_photo',
    )


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}, {self.created_at} by {self.user}'
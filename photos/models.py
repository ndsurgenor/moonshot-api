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
    title = models.CharField(max_length=127, blank=False)
    main_feature = models.CharField(
        max_length=127, choices=MAIN_FEATURES
    )
    description = models.TextField(blank=True)
    location = models.CharField(max_length=127, blank=True)
    photo_date = models.DateField()
    photo_time = models.TimeField()
    # Should autpopulate from 'main_lens' field on Equipment Profile model
    lens_used = models.CharField(max_length=127, blank=True)
    # Should autpopulate from 'main_camera' field on Equipment Profile model
    camera_used = models.CharField(max_length=127, blank=True)
    # Should autpopulate from 'other_equipment' field on Equipment Profile model
    other_equipment_used = models.TextField(max_length=127, blank=True)
    image = models.ImageField(
        upload_to='images/',
        default = '../default_photo'
    )


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}, {self.created_at} by {self.user}'
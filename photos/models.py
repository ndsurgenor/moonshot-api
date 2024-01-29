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
    title = models.CharField(max_length=127, blank=True)
    main_feature = models.IntegerField(choices=MAIN_FEATURES)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=127, blank=True)
    date_taken = models.DateField()
    time_taken = models.TimeField()
    equipment = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default = '../default_photo'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} by {self.user}'
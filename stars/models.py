from django.db import models
from django.contrib.auth.models import User
from photos.models import Photo
from .variables import STAR_VALUES


class Star(models.Model):
    """
    Star model associated with a specific user and photo
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name='stars')
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(choices=STAR_VALUES)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'photo']

    def __str__(self):
        return f'{self.user}: {self.value} for {self.photo}'
from django.db import models
from django.contrib.auth.models import User
from photos.models import Photo


class Star(models.Model):
    """
    Star model associated with a specific photo and user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name='stars')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'photo']

    def __str__(self):
        return f'{self.user}{self.photo}'
from django.db import models
from django.contrib.auth.models import User

class EquipmentProfile(models.Model):
    """
    Creates an Equipment Profile connected to a specific user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    lens = models.CharField(max_length=127, blank=True)
    camera = models.CharField(max_length=127, blank=True)
    other_equipment = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Equipment Profile for {self.user}'
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class EquipmentProfile(models.Model):
    """
    Creates an Equipment Profile connected to a specific user
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    main_lens = models.CharField(
        max_length=127,
        default="",
        blank=True,
        null=True,
    )
    main_camera = models.CharField(
        max_length=127,
        default="",
        blank=True,
        null=True,
    )
    other_equipment = models.TextField(
        max_length=255,
        default="",
        blank=True,
        null=True,
    )


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Equipment Profile for {self.user}'


# Automatically creates an Equipment Profile for a user when they sign up
def create_equipment_profile(sender, instance, created, **kwargs):
    if created:
        EquipmentProfile.objects.create(user=instance)

post_save.connect(create_equipment_profile, sender=User)
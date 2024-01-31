from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Creates a user profile automatically when a new user signs up
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=127, blank=True)
    details = models.TextField(blank=True)
    avatar = models.ImageField(
        upload_to='images/',
        default = '../default_avatar'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'User Profile for {self.user}'


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
# Create user profile

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profiles/', null=True)
    user_bio = models.TextField()
    user = models.OneToOneField(User)
    last_update = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-last_update']

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

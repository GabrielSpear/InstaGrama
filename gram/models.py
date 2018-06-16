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


# Create Image function
class Image(models.Model):
    image = models.ImageField(upload_to='photos/', null=True)
    image_name = models.CharField(max_length=30, null=True)
    image_caption = models.TextField(null=True)
    likes = models.IntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile, null=True)

    class Meta:
        ordering = ['-date_uploaded']

    def save_image(self):
        self.save()

    @classmethod
    def search_by_user(cls, search_term):
        images = cls.objects.filter(image_caption__icontains=search_term)
        return images

    @classmethod
    def get_image_by_id(cls, image_id):
        images = cls.objects.get(id=image_id)
        return images

# Create comment function

class Comments(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True)
    image = models.ForeignKey(Image, null=True)
    time_comment = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-time_comment']

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from os import path
from PIL import Image
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver



def get_profile_picture_filepath(instance, filename):
    filename = filename.split('.')[-1]
    return path.join('profile_images', '{}profile_image.{}'.format(instance.pk, filename))

class User(AbstractUser):
    
    class Meta:
        permissions = (
            ("client", "Client"),
            ("support", "Support"),
        )

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE , related_name='profile')

    avatar = models.ImageField(default='avatar/avatar.PNG', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    def get_update_url(self):
        return reverse("users:Update_Profile3", args=(self.user.pk,))

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

class OtpCode(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.code



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


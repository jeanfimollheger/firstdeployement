from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# Create your models here.
class Member(AbstractUser):
    # Additional fields can be added here
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)


    def __str__(self):
        return self.username


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return f"/members/{self.slug}/"

    
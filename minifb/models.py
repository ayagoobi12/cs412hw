from django.db import models

# Create your models here.
class Profile(models.Model):
    """Encapsulate the idea of a facebook profile"""
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email_address = models.TextField(blank=False)
    profile_image_url = models.URLField(blank=True) ## new

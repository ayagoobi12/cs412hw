from django.db import models

# Create your models here.
class Profile(models.Model):
    """Encapsulate the idea of a facebook profile"""
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email_address = models.TextField(blank=False)
    profile_image_url = models.URLField(blank=True) ## new

    def get_status_messages(self):
        """Retrieve all status messages related to this profile, ordered by timestamp."""
        return self.status_messages.all().order_by('timestamp')  # 'status_messages' comes from the related_name in StatusMessage


class StatusMessage(models.Model):
    timestamp = models.DateTimeField()  # Manually set the creation time of the status message
    message = models.TextField()  # The text of the status message
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name ='status_messages')  # Foreign key to Profile

    def __str__(self):
        return f"Status from {self.profile}: {self.message[:20]}..."  # Optional string representation
    


    
    
    

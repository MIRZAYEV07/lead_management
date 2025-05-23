from django.db import models

#something
class Lead(models.Model):
    STATE_CHOICES = [
        ("PENDING", "Pending"),
        ("REACHED_OUT", "Reached Out"),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

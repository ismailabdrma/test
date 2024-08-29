from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=255, blank=True, null=True)  # Optional location description
    latitude = models.FloatField(blank=True, null=True)  # Optional latitude
    longitude = models.FloatField(blank=True, null=True)  # Optional longitude
    image = models.ImageField(upload_to='reports/', blank=True, null=True)
    status = models.CharField(max_length=50, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

